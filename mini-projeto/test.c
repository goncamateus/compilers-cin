int returnInt() {
	return 1;
}

float returnFloat() {
	return 4.3;
}

boolean returnBoolean() {
	return 1;
}

int declarationTest() {
	int varDeclarationTest;
	float varDeclarationTest2;
	boolean varDeclarationTest3;
	return 0;
}

int returnArgIntTest(int argIntTest) {
	return argIntTest;
}

float returnArgFloatTest(float argFloatTest) {
	return argFloatTest;
}

boolean returnArgBooleanTest(boolean argBooleanTest) {
	return argBooleanTest;
}

int assignTest() {
	int  varAssignTest = 2;
	int  varAssignTest2 = 3;
	float varAssignTest3 = 2.2;
	boolean varAssignTest4 = 1;
	varAssignTest = varAssignTest2;
	varAssignTest4 = 0;
	return 0;
}

int numOperationTest() {
	int varNumOperationTest = 2 + 2;
	varNumOperationTest = 2 - 2;
	varNumOperationTest = 2 * 2;
	varNumOperationTest = 2 / 2;
	float varNumOperationTest2 = 2.9 + 0.1;
	varNumOperationTest2 = 2.9 - 0.2;
	varNumOperationTest2 = 2.75 * 8.43;
	varNumOperationTest2 = 1.0 / 0.5;
	return 0;
}

boolean booleanOperationTest() {
	boolean varBooleanOperationTest = 1 && 1;
	boolean varNumOperationTest = 2 > 1;
	varBooleanOperationTest = 0 || 0;
	varNumOperationTest = 2 < 1;
	varNumOperationTest = 2 == 1;
	varNumOperationTest = 2 != 1;
	return 1;
}

int multipleArgsTest(int argTest1, int argTest2, int argTest3, int argTest4) {
	int varMultipleArgsTest = argTest1 + argTest2 + argTest3 + argTest4;
	return varMultipleArgsTest;
}

int ifTest() {
	boolean varIfTest = 1;
	if (1) {
		if (varIfTest) {
			varIfTest = 0;
		}
		else if (!varIfTest == 0) {
			varIfTest = 1;
		}
	}
	else {
		varIfTest = varIfTest;
	}
	return 0;
}

int callTest() {
	int varCallTest = returnInt();
	float varCallTest2 = returnFloat();
	// varCallTest = ifTest();
	varCallTest = multipleArgsTest(1, 2, 3, 4);
	return 0;
}