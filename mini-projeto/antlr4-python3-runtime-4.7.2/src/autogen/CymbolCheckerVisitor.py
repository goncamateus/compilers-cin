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

    def visitFiile(self, ctx: CymbolParser.FiileContext):
        print(self.start_file_str)
        self.visitChildren(ctx)
        print('\n', self.attrs_str, '\n\n')
        print(self.llvm_config, '\n\n')
        print(self.clang_config, '\n')

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
        # self.visit(ctx.paramTypeList())
        param_string = "() #0 "
        block_string = self.visit(ctx.block())
        block_string = block_string.replace('ret xxxange', 'ret ' + ret_type)
        print(func_str + param_string + block_string)

    def visitBlock(self, ctx: CymbolParser.BlockContext):
        result = "{"
        lastResult = None
        first = 0
        vars_in_block = 0
        var_list = []
        if ctx.stat() is not None:
            al = ctx.stat()
            for x in al:
                if x.returnStat() is not None:
                    ret = self.visit(x.returnStat())
                    if ret in var_list:
                        ret = var_list.index(ret) + 1
                    ret_str = "\n  ret xxxange {}".format(ret)
                    result += ret_str
                else:
                    if x.assignStat() is not None:
                        self.visit(x.assignStat())
                    if x.exprStat() is not None:
                        self.visit(x.exprStat())
                    if x.varDecl() is not None:
                        var_decl_string, var_name = self.visit(x.varDecl())
                        vars_in_block += 1
                        var_decl_string = var_decl_string.replace(
                            "change", str(vars_in_block))
                        result += var_decl_string
                        var_list.append(var_name)

        result += "\n}\n\n"
        return result

    def visitVarDecl(self, ctx: CymbolParser.VarDeclContext):
        var_name = ctx.ID().getText()
        tyype = ctx.tyype().getText()
        if tyype == Type.INT:
            tyype = 'i32'
        elif tyype == Type.BOOLEAN:
            tyype = 'i8'
        vardecl_str = "\n  %{} = alloca {}, align {}".format(
            "change", tyype, "4" if tyype != "i8" else "1")
        if (tyype == Type.VOID):
            result = Type.VOID
            print("Mensagem de erro 1...")
            exit(1)
        else:
            if ctx.expr() != None:
                init = ctx.expr()
                # print("init = ", init)

        return vardecl_str, var_name

    def visitReturnStat(self, ctx: CymbolParser.ReturnStatContext):
        result = Type.VOID
        if ctx.expr() != None:
            result = self.visit(ctx.expr())

        if not isinstance(result, str):
            result = str(result)
        return result

    def aggregateResult(self, aggregate: Type, next_result: Type):
        return next_result if next_result != None else aggregate
