from antlr4 import *
from autogen.CymbolParser import CymbolParser
from autogen.CymbolVisitor import CymbolVisitor
import struct


def printError(ctx):
    print("erro: operador '", ctx.op.text, "' na linha", (ctx.op.line), ",coluna", (ctx.op.column),
          "indefinidos para os tipos")


def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])


class Type:
    VOID = "void"
    INT = "int"
    FLOAT = "float"
    BOOLEAN = "boolean"


class CymbolCheckerVisitor(CymbolVisitor):
    id_values = {}
    start_file_str = "; ModuleID = \'test.c\'\nsource_filename = \"test.c\"\ntarget datalayout = \"e-m:e-i64:64-f80:128-n8:16:32:64-S128\"\ntarget triple = \"x86_64-pc-linux-gnu\""
    attrs_str = "attributes #0 = { noinline nounwind optnone uwtable \"correctly-rounded-divide-sqrt-fp-math\"=\"false\" \"disable-tail-calls\"=\"false\" \"less-precise-fpmad\"=\"false\" \"no-frame-pointer-elim\"=\"true\" \"no-frame-pointer-elim-non-leaf\" \"no-infs-fp-math\"=\"false\" \"no-jump-tables\"=\"false\" \"no-nans-fp-math\"=\"false\" \"no-signed-zeros-fp-math\"=\"false\" \"no-trapping-math\"=\"false\" \"stack-protector-buffer-size\"=\"8\" \"target-cpu\"=\"x86-64\" \"target-features\"=\"+fxsr,+mmx,+sse,+sse2,+x87\" \"unsafe-fp-math\"=\"false\" \"use-soft-float\"=\"false\" }"
    llvm_config = "!llvm.module.flags = !{!0}\n!llvm.ident = !{!1}"
    clang_config = "!1 = !{!\"clang version 6.0.0-1ubuntu2 (tags/RELEASE_600/final)\"}"
    funct_init_str = "; Function Attrs: noinline nounwind optnone uwtable\n"
    func_vars = {}
    func_params = {}
    funcs_types = {}
    actual_func_type = None
    var_list = []
    alignes = {
        'i32': 4,
        'float': 4,
        'i8': 1
    }

    # OK
    def visitFiile(self, ctx: CymbolParser.FiileContext):
        print(self.start_file_str)
        self.visitChildren(ctx)
        print('\n', self.attrs_str, '\n\n')
        print(self.llvm_config, '\n\n')
        print(self.clang_config, '\n')

    # OK

    def visitParamTypeList(self, ctx: CymbolParser.ParamTypeListContext):
        params = [x for x in ctx.children if isinstance(
            x, CymbolParser.ParamTypeContext)]
        params_dict = {}
        param_list_str = "("
        for param in params:
            tyype, param_id = self.visit(param)
            tipo = tyype
            if tipo == Type.INT:
                tipo = "i32"
            elif tipo == Type.BOOLEAN:
                tipo = "i1 zeroext"
            params_dict[param_id] = tipo
            param_list_str += tipo
            if param != params[-1]:
                param_list_str += ", "
        param_list_str += ') #0 '
        return param_list_str, params_dict

    # OK
    def visitParamType(self, ctx: CymbolParser.ParamTypeContext):
        return ctx.tyype().getText(), ctx.ID().getText()

    # OK
    def visitFuncDecl(self, ctx: CymbolParser.FuncDeclContext):
        tyype = ctx.tyype().getText()
        func_id = ctx.ID().getText()
        tipo = ret_type = tyype
        if tipo == Type.INT:
            tipo = ret_type = "i32"
        elif tipo == Type.BOOLEAN:
            tipo = "zeroext i1"
            ret_type = "i1"
        func_str = self.funct_init_str
        func_str += "define {} @{}".format(tipo, func_id)
        param_string = "() #0 "
        param_dict = None
        self.actual_func_type = tipo
        if ctx.paramTypeList() is not None:
            param_string, param_dict = self.visit(ctx.paramTypeList())
            self.func_params = param_dict
            self.var_list = list(self.func_params.keys())
            for key, value in param_dict.items():
                self.func_vars[key] = (0, value)

        block_string = self.visit(ctx.block())
        block_string = block_string.replace('ret xxxange', 'ret ' + ret_type)
        self.func_params = {}
        self.func_vars = {}
        self.funcs_types[func_id] = tipo
        print(func_str + param_string + block_string)

    def visitBlock(self, ctx: CymbolParser.BlockContext):
        result = "{"
        lastResult = None
        first = 0
        if ctx.stat() is not None:
            al = ctx.stat()
            for x in al:
                if x.returnStat() is not None:
                    ret = self.visit(x.returnStat())
                    ret_str = "\n  ret xxxange {}".format(ret[0])
                    result += ret[1] + ret_str
                else:
                    if x.assignStat() is not None:
                        result_assing = self.visit(x.assignStat())
                        result += result_assing
                    if x.exprStat() is not None:
                        self.visit(x.exprStat())
                    if x.varDecl() is not None:
                        var_decl_string, var_name = self.visit(x.varDecl())
                        result += var_decl_string

        result += "\n}\n\n"
        self.var_list = []
        return result

    def visitVarDecl(self, ctx: CymbolParser.VarDeclContext):
        var_name = ctx.ID().getText()
        tyype = tipo = ctx.tyype().getText()
        if tipo == Type.INT:
            tipo = 'i32'
        elif tipo == Type.BOOLEAN:
            tipo = 'i8'
        self.var_list.append(var_name)
        vardecl_str = "\n  %{} = alloca {}, align {}".format(
            self.var_list.index(var_name) + 1, tipo, self.alignes[tipo])
        if ctx.expr() != None:
            self.func_vars[var_name] = (0, tipo)
            result, expr_str = self.visit(ctx.expr())
            self.func_vars[var_name] = (result, tipo)
            vardecl_str += expr_str

        return vardecl_str, var_name

    # OK
    def visitReturnStat(self, ctx: CymbolParser.ReturnStatContext):
        result = None
        if ctx.expr() != None:
            result, expr_str = self.visit(ctx.expr())

        return result, expr_str

    # OK
    def visitAssignStat(self, ctx: CymbolParser.AssignStatContext):
        var_name = ctx.ID().getText()
        idx = self.var_list.index(var_name) + 1
        tipo = self.func_vars[var_name][1]

        result = None
        expr_str = ""
        if ctx.expr():
            result, expr_str = self.visit(ctx.expr())

        assign_str = "\n  store {} {}, {}* %{}, align {}".format(
            tipo, result, tipo, idx, self.alignes[tipo])
        if "%" in result:
            assign_str = expr_str + assign_str
        return assign_str

    def visitExprStat(self, ctx: CymbolParser.ExprStatContext):
        result = tmp_var_idx = None
        if ctx.expr() != None:
            result = self.visit(ctx.expr())

        return result

    def visitExprList(self, ctx: CymbolParser.ExprListContext):
        exprs = [x for x in ctx.children if isinstance(
            x, CymbolParser.ExprContext)]
        expr_list_str = ""
        for expr in exprs:
            result = self.visit(expr)
            if result is not None:
                tmp_var_idx, vis_string = result
                tipo = self.func_vars['%{}'.format(tmp_var_idx + 1)][1]
                expr_list_str += "{} {}".format(tipo, tmp_var_idx)
                if expr != exprs[-1]:
                    expr_list_str += ", "

        return expr_list_str

    def visitExpr(self, ctx: CymbolParser.ExprContext):
        # Com ID
        if ctx.ID() is not None:
            # func call
            if ctx.ID().getText() in self.funcs_types.keys():
                tmp_var_idx = len(self.var_list) + 1
                tmp_var_str = "%" + str(tmp_var_idx)
                self.var_list.append(tmp_var_str)

                func_id = ctx.ID().getText()
                func_type = self.funcs_types[func_id]
                expr_str = "\n  "
                expr_str += "%{} = call {} @{}(".format(tmp_var_idx,
                                                        func_type, func_id)
                expr_list = ""
                if ctx.exprList() is not None:
                    expr_list = self.visit(ctx.exprList())
                expr_str += expr_list + ")\n"
                return tmp_var_str, expr_str
            else:
                hm_vars = len(self.var_list)
                tmp_idx = hm_vars + 1
                full_str = ""
                real_ret = None
                # Param sanity
                if ctx.ID().getText() in self.func_params.keys():
                    tipo = self.func_params[ctx.ID().getText()]
                    if tipo == "i1 zeroext":
                        tipo = "i8"
                        new_tmp_str = "\n  %{} = alloca {}, align 1\n".format(
                            tmp_idx, tipo)
                        self.var_list.append("%{}".format(hm_vars + 1))
                        self.func_vars["%{}".format(hm_vars + 1)] = tipo
                        zext_str = "  %{} = zext i1 %{} to i8\n".format(
                            hm_vars + 2, self.var_list.index(ctx.ID().getText()))
                        self.var_list.append("%{}".format(hm_vars + 2))
                        self.func_vars["%{}".format(hm_vars + 2)] = tipo
                        store_str = "  store {} %{}, {}* %{}, align 4\n".format(
                            tipo,  hm_vars + 2, tipo, hm_vars + 1)
                        self.var_list.append("%{}".format(hm_vars + 3))
                        self.func_vars["%{}".format(hm_vars + 3)] = tipo
                        trunc_str = "  %{} = trunc i8 %{} to i1".format(
                            hm_vars + 4, hm_vars + 3)
                        self.var_list.append("%{}".format(hm_vars + 4))
                        self.func_vars["%{}".format(hm_vars + 4)] = tipo
                        real_ret = "%"+str(hm_vars + 4)
                        full_str = new_tmp_str + zext_str + store_str + trunc_str
                    else:
                        new_tmp_str = "\n  %{} = alloca {}, align 4\n".format(
                            tmp_idx, tipo)
                        self.var_list.append("%{}".format(hm_vars + 1))
                        self.func_vars["%{}".format(hm_vars + 1)] = tipo
                        store_str = "  store {} %{}, {}* %{}, align 4\n".format(
                            tipo, self.var_list.index(ctx.ID().getText()), tipo, hm_vars + 1)
                        self.var_list.append("%{}".format(hm_vars + 2))
                        self.func_vars["%{}".format(hm_vars + 2)] = tipo
                        load_str = "  %{} = load {}, {}* %{}, align 4\n".format(
                            hm_vars + 2, tipo, tipo, hm_vars + 1)
                        full_str = new_tmp_str + store_str + load_str
                        real_ret = "%"+str(hm_vars + 2)
                # Assign com ID
                elif ctx.ID().getText() in self.func_vars.keys():
                    new_idx = len(self.var_list) + 1
                    idx = self.var_list.index(ctx.ID().getText()) + 1
                    tipo = self.func_vars[ctx.ID().getText()][1]
                    full_str = "\n  %{} = load {}, {}* %{}, align {}".format(
                        new_idx, tipo, tipo, idx, self.alignes[tipo])
                    real_ret = "%" + str(new_idx)
                return real_ret, full_str
        # Numeros em geral
        if ctx.op is None and "!" not in ctx.getText() and "(" not in ctx.getText():
            if isinstance(ctx.parentCtx, CymbolParser.ReturnStatContext):
                if ctx.INT() is not None:
                    return ctx.INT().getText(), ""
                if ctx.FLOAT() is not None:
                    real_ret = float(ctx.FLOAT().getText())
                    real_ret = float_to_hex(real_ret)
                    return real_ret, ""
                if ctx.BOOLEAN() is not None:
                    return ctx.BOOLEAN().getText(), ""
            elif isinstance(ctx.parentCtx, CymbolParser.VarDeclContext):
                tipo = self.func_vars[ctx.parentCtx.ID().getText()][1]
                if ctx.INT() is not None:
                    assign_str = "\n  store {} {}, {}* %{}, align {}".format(
                        tipo, ctx.INT().getText(), tipo, len(self.var_list), self.alignes[tipo])
                    return ctx.INT().getText(), assign_str
                if ctx.FLOAT() is not None:
                    real_ret = float(ctx.FLOAT().getText())
                    real_ret = float_to_hex(real_ret)
                    assign_str = "\n  store {} {}, {}* %{}, align {}".format(
                        tipo, real_ret, tipo, len(self.var_list), self.alignes[tipo])
                    return real_ret, assign_str
                if ctx.BOOLEAN() is not None:
                    assign_str = "\n  store {} {}, {}* %{}, align {}".format(
                        tipo, ctx.BOOLEAN().getText(), tipo, len(self.var_list), self.alignes[tipo])
                    return ctx.BOOLEAN().getText(), assign_str
            else:
                if ctx.INT() is not None:
                    return ctx.INT().getText(), ""
                if ctx.FLOAT() is not None:
                    real_ret = float(ctx.FLOAT().getText())
                    real_ret = float_to_hex(real_ret)
                    return real_ret, ""
                if ctx.BOOLEAN() is not None:
                    return ctx.BOOLEAN().getText(), ""
        # Operacoes
        if ctx.op is not None:
            left = ctx.expr()[0].accept(self)
            right = ctx.expr()[1].accept(self)
            if "%" in left or "%" in right:
                print('pintamanhagaba')
            else:
                var = ctx.parentCtx.ID().getText()
                tipo = self.func_vars[var][1]
                idx = self.var_list.index(var) + 1
                res = 0
                store_str = ""
                right = right[0]
                left = left[0]
                if tipo == "float":
                    right = 1
                    left = 1
                    # right = struct.unpack('!f', right.decode('hex'))[0]
                    # left = struct.unpack('!f', left.decode('hex'))[0]
                else:
                    right = int(right)
                    left = int(left)
                if ctx.op.text == "+":
                    res = right + left
                elif ctx.op.text == "-":
                    res = right - left
                elif ctx.op.text == "*":
                    res = right * left
                elif ctx.op.text == "/":
                    res = right / left
                elif ctx.op.text == "&&":
                    res = right and left
                elif ctx.op.text == "||":
                    res = right or left
                elif ctx.op.text == "==":
                    res = right == left
                elif ctx.op.text == "!=":
                    res = right != left
                if tipo == "float":
                    res = float_to_hex(res)
                if tipo != 'float':
                    res = int(res)
                store_str = "\n  store {} {}, {}* %{}, align {}".format(tipo, res, tipo, idx, self.alignes[tipo])
            return str(res), store_str
                
                
    def aggregateResult(self, aggregate: Type, next_result: Type):
        return next_result if next_result != None else aggregate
