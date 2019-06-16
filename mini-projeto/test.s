	.text
	.file	"test.c"
	.globl	returnInt               # -- Begin function returnInt
	.p2align	4, 0x90
	.type	returnInt,@function
returnInt:                              # @returnInt
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movl	$1, %eax
	popq	%rbp
	retq
.Lfunc_end0:
	.size	returnInt, .Lfunc_end0-returnInt
	.cfi_endproc
                                        # -- End function
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2               # -- Begin function returnFloat
.LCPI1_0:
	.long	1082759578              # float 4.30000019
	.text
	.globl	returnFloat
	.p2align	4, 0x90
	.type	returnFloat,@function
returnFloat:                            # @returnFloat
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movss	.LCPI1_0(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	popq	%rbp
	retq
.Lfunc_end1:
	.size	returnFloat, .Lfunc_end1-returnFloat
	.cfi_endproc
                                        # -- End function
	.globl	returnBoolean           # -- Begin function returnBoolean
	.p2align	4, 0x90
	.type	returnBoolean,@function
returnBoolean:                          # @returnBoolean
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movb	$1, %al
	andb	$1, %al
	movzbl	%al, %eax
	popq	%rbp
	retq
.Lfunc_end2:
	.size	returnBoolean, .Lfunc_end2-returnBoolean
	.cfi_endproc
                                        # -- End function
	.globl	declarationTest         # -- Begin function declarationTest
	.p2align	4, 0x90
	.type	declarationTest,@function
declarationTest:                        # @declarationTest
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	xorl	%eax, %eax
	popq	%rbp
	retq
.Lfunc_end3:
	.size	declarationTest, .Lfunc_end3-declarationTest
	.cfi_endproc
                                        # -- End function
	.globl	returnArgIntTest        # -- Begin function returnArgIntTest
	.p2align	4, 0x90
	.type	returnArgIntTest,@function
returnArgIntTest:                       # @returnArgIntTest
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movl	%edi, -4(%rbp)
	movl	-4(%rbp), %eax
	popq	%rbp
	retq
.Lfunc_end4:
	.size	returnArgIntTest, .Lfunc_end4-returnArgIntTest
	.cfi_endproc
                                        # -- End function
	.globl	returnArgFloatTest      # -- Begin function returnArgFloatTest
	.p2align	4, 0x90
	.type	returnArgFloatTest,@function
returnArgFloatTest:                     # @returnArgFloatTest
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movss	%xmm0, -4(%rbp)
	movss	-4(%rbp), %xmm0         # xmm0 = mem[0],zero,zero,zero
	popq	%rbp
	retq
.Lfunc_end5:
	.size	returnArgFloatTest, .Lfunc_end5-returnArgFloatTest
	.cfi_endproc
                                        # -- End function
	.globl	returnArgBooleanTest    # -- Begin function returnArgBooleanTest
	.p2align	4, 0x90
	.type	returnArgBooleanTest,@function
returnArgBooleanTest:                   # @returnArgBooleanTest
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	andb	$1, %dil
	movb	%dil, -1(%rbp)
	movb	-1(%rbp), %al
	andb	$1, %al
	movzbl	%al, %eax
	popq	%rbp
	retq
.Lfunc_end6:
	.size	returnArgBooleanTest, .Lfunc_end6-returnArgBooleanTest
	.cfi_endproc
                                        # -- End function
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2               # -- Begin function assignTest
.LCPI7_0:
	.long	1074580685              # float 2.20000005
	.text
	.globl	assignTest
	.p2align	4, 0x90
	.type	assignTest,@function
assignTest:                             # @assignTest
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movss	.LCPI7_0(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movl	$2, -12(%rbp)
	movl	$3, -8(%rbp)
	movss	%xmm0, -16(%rbp)
	movb	$1, -1(%rbp)
	movl	-8(%rbp), %eax
	movl	%eax, -12(%rbp)
	movb	$0, -1(%rbp)
	xorl	%eax, %eax
	popq	%rbp
	retq
.Lfunc_end7:
	.size	assignTest, .Lfunc_end7-assignTest
	.cfi_endproc
                                        # -- End function
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2               # -- Begin function numOperationTest
.LCPI8_0:
	.long	1073741824              # float 2
.LCPI8_1:
	.long	1102673347              # float 23.1825008
.LCPI8_2:
	.long	1076677837              # float 2.70000005
.LCPI8_3:
	.long	1077936128              # float 3
	.text
	.globl	numOperationTest
	.p2align	4, 0x90
	.type	numOperationTest,@function
numOperationTest:                       # @numOperationTest
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movss	.LCPI8_0(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movss	.LCPI8_1(%rip), %xmm1   # xmm1 = mem[0],zero,zero,zero
	movss	.LCPI8_2(%rip), %xmm2   # xmm2 = mem[0],zero,zero,zero
	movss	.LCPI8_3(%rip), %xmm3   # xmm3 = mem[0],zero,zero,zero
	movl	$4, -8(%rbp)
	movl	$0, -8(%rbp)
	movl	$4, -8(%rbp)
	movl	$1, -8(%rbp)
	movss	%xmm3, -4(%rbp)
	movss	%xmm2, -4(%rbp)
	movss	%xmm1, -4(%rbp)
	movss	%xmm0, -4(%rbp)
	xorl	%eax, %eax
	popq	%rbp
	retq
.Lfunc_end8:
	.size	numOperationTest, .Lfunc_end8-numOperationTest
	.cfi_endproc
                                        # -- End function
	.globl	_BoolOperationTest      # -- Begin function _BoolOperationTest
	.p2align	4, 0x90
	.type	_BoolOperationTest,@function
_BoolOperationTest:                     # @_BoolOperationTest
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movb	$1, %al
	movb	$1, -2(%rbp)
	movb	$1, -1(%rbp)
	movb	$0, -2(%rbp)
	movb	$0, -1(%rbp)
	movb	$0, -1(%rbp)
	movb	$1, -1(%rbp)
	andb	$1, %al
	movzbl	%al, %eax
	popq	%rbp
	retq
.Lfunc_end9:
	.size	_BoolOperationTest, .Lfunc_end9-_BoolOperationTest
	.cfi_endproc
                                        # -- End function
	.globl	multipleArgsTest        # -- Begin function multipleArgsTest
	.p2align	4, 0x90
	.type	multipleArgsTest,@function
multipleArgsTest:                       # @multipleArgsTest
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movl	%edi, -20(%rbp)
	movl	%esi, -16(%rbp)
	movl	%edx, -12(%rbp)
	movl	%ecx, -8(%rbp)
	movl	-20(%rbp), %eax
	addl	-16(%rbp), %eax
	addl	-12(%rbp), %eax
	addl	-8(%rbp), %eax
	movl	%eax, -4(%rbp)
	movl	-4(%rbp), %eax
	popq	%rbp
	retq
.Lfunc_end10:
	.size	multipleArgsTest, .Lfunc_end10-multipleArgsTest
	.cfi_endproc
                                        # -- End function
	.globl	ifTest                  # -- Begin function ifTest
	.p2align	4, 0x90
	.type	ifTest,@function
ifTest:                                 # @ifTest
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movb	$1, -1(%rbp)
	testb	$1, -1(%rbp)
	je	.LBB11_2
# %bb.1:
	movb	$0, -1(%rbp)
	jmp	.LBB11_5
.LBB11_2:
	movb	-1(%rbp), %al
	xorb	$-1, %al
	andb	$1, %al
	movzbl	%al, %eax
	cmpl	$0, %eax
	jne	.LBB11_4
# %bb.3:
	movb	$1, -1(%rbp)
.LBB11_4:
	jmp	.LBB11_5
.LBB11_5:
	xorl	%eax, %eax
	popq	%rbp
	retq
.Lfunc_end11:
	.size	ifTest, .Lfunc_end11-ifTest
	.cfi_endproc
                                        # -- End function
	.globl	callTest                # -- Begin function callTest
	.p2align	4, 0x90
	.type	callTest,@function
callTest:                               # @callTest
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$16, %rsp
	callq	returnInt
	movl	%eax, -4(%rbp)
	callq	returnFloat
	movss	%xmm0, -8(%rbp)
	callq	ifTest
	movl	%eax, -4(%rbp)
	movl	$1, %edi
	movl	$2, %esi
	movl	$3, %edx
	movl	$4, %ecx
	callq	multipleArgsTest
	movl	%eax, -4(%rbp)
	xorl	%eax, %eax
	addq	$16, %rsp
	popq	%rbp
	retq
.Lfunc_end12:
	.size	callTest, .Lfunc_end12-callTest
	.cfi_endproc
                                        # -- End function

	.ident	"clang version 6.0.0-1ubuntu2 (tags/RELEASE_600/final)"
	.section	".note.GNU-stack","",@progbits
