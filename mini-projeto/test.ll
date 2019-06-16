; ModuleID = 'test.c'
source_filename = "test.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: noinline nounwind optnone uwtable
define i32 @returnInt() #0 {
  ret i32 1
}

; Function Attrs: noinline nounwind optnone uwtable
define float @returnFloat() #0 {
  ret float 0x4011333340000000
}

; Function Attrs: noinline nounwind optnone uwtable
define zeroext i1 @returnBoolean() #0 {
  ret i1 true
}

; Function Attrs: noinline nounwind optnone uwtable
define i32 @declarationTest() #0 {
  %1 = alloca i32, align 4
  %2 = alloca float, align 4
  %3 = alloca i8, align 1
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define i32 @returnArgIntTest(i32) #0 {
  %2 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  %3 = load i32, i32* %2, align 4
  ret i32 %3
}

; Function Attrs: noinline nounwind optnone uwtable
define float @returnArgFloatTest(float) #0 {
  %2 = alloca float, align 4
  store float %0, float* %2, align 4
  %3 = load float, float* %2, align 4
  ret float %3
}

; Function Attrs: noinline nounwind optnone uwtable
define zeroext i1 @returnArgBooleanTest(i1 zeroext) #0 {
  %2 = alloca i8, align 1
  %3 = zext i1 %0 to i8
  store i8 %3, i8* %2, align 1
  %4 = load i8, i8* %2, align 1
  %5 = trunc i8 %4 to i1
  ret i1 %5
}

; Function Attrs: noinline nounwind optnone uwtable
define i32 @assignTest() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca float, align 4
  %4 = alloca i8, align 1
  store i32 2, i32* %1, align 4
  store i32 3, i32* %2, align 4
  store float 0x40019999A0000000, float* %3, align 4
  store i8 1, i8* %4, align 1
  %5 = load i32, i32* %2, align 4
  store i32 %5, i32* %1, align 4
  store i8 0, i8* %4, align 1
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define i32 @numOperationTest() #0 {
  %1 = alloca i32, align 4
  store i32 4, i32* %1, align 4
  store i32 0, i32* %1, align 4
  store i32 4, i32* %1, align 4
  store i32 1, i32* %1, align 4
  %2 = alloca float, align 4
  store float 3.000000e+00, float* %2, align 4
  store float 0x40059999A0000000, float* %2, align 4
  store float 0x40372EB860000000, float* %2, align 4
  store float 2.000000e+00, float* %2, align 4
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define zeroext i1 @_BoolOperationTest() #0 {
  %1 = alloca i8, align 1
  %2 = alloca i8, align 1
  store i8 1, i8* %1, align 1
  store i8 1, i8* %2, align 1
  store i8 0, i8* %1, align 1
  store i8 0, i8* %2, align 1
  store i8 0, i8* %2, align 1
  store i8 1, i8* %2, align 1
  ret i1 true
}

; Function Attrs: noinline nounwind optnone uwtable
define i32 @multipleArgsTest(i32, i32, i32, i32) #0 {
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i32, align 4
  %9 = alloca i32, align 4
  store i32 %0, i32* %5, align 4
  store i32 %1, i32* %6, align 4
  store i32 %2, i32* %7, align 4
  store i32 %3, i32* %8, align 4
  %10 = load i32, i32* %5, align 4
  %11 = load i32, i32* %6, align 4
  %12 = add nsw i32 %10, %11
  %13 = load i32, i32* %7, align 4
  %14 = add nsw i32 %12, %13
  %15 = load i32, i32* %8, align 4
  %16 = add nsw i32 %14, %15
  store i32 %16, i32* %9, align 4
  %17 = load i32, i32* %9, align 4
  ret i32 %17
}

; Function Attrs: noinline nounwind optnone uwtable
define i32 @ifTest() #0 {
  %1 = alloca i8, align 1
  store i8 1, i8* %1, align 1
  %2 = load i8, i8* %1, align 1
  %3 = trunc i8 %2 to i1
  br i1 %3, label %4, label %5

; <label>:4:                                      ; preds = %0
  store i8 0, i8* %1, align 1
  br label %13

; <label>:5:                                      ; preds = %0
  %6 = load i8, i8* %1, align 1
  %7 = trunc i8 %6 to i1
  %8 = xor i1 %7, true
  %9 = zext i1 %8 to i32
  %10 = icmp eq i32 %9, 0
  br i1 %10, label %11, label %12

; <label>:11:                                     ; preds = %5
  store i8 1, i8* %1, align 1
  br label %12

; <label>:12:                                     ; preds = %11, %5
  br label %13

; <label>:13:                                     ; preds = %12, %4
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define i32 @callTest() #0 {
  %1 = alloca i32, align 4
  %2 = alloca float, align 4
  %3 = call i32 @returnInt()
  store i32 %3, i32* %1, align 4
  %4 = call float @returnFloat()
  store float %4, float* %2, align 4
  %5 = call i32 @ifTest()
  store i32 %5, i32* %1, align 4
  %6 = call i32 @multipleArgsTest(i32 1, i32 2, i32 3, i32 4)
  store i32 %6, i32* %1, align 4
  ret i32 0
}

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 6.0.0-1ubuntu2 (tags/RELEASE_600/final)"}
