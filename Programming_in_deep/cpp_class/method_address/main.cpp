#include <iostream>

class TestClass {
private:
	int mem;
	void (TestClass::*fptr) (void);
public:
	TestClass(int _mem) {
		mem = _mem;
	}
	
	void test_method() {
		std::cout << "method called\n" << std::endl;
	}
	void print_method_addr(){
		fptr = &TestClass::test_method;
		std::cout << mem << "  " << &fptr << std::endl;
	}
};


int main() {
	TestClass test_obj1(1);
	TestClass test_obj2(2);
	TestClass test_obj3(3);
	TestClass test_obj4(4);
	TestClass test_obj5(5);
	test_obj1.test_method();
	
	test_obj1.print_method_addr();
	std::cout << "----------" << std::endl;
	test_obj2.print_method_addr();
	std::cout << "----------" << std::endl;
	test_obj3.print_method_addr();
	std::cout << "----------" << std::endl;
	test_obj4.print_method_addr();
	std::cout << "----------" << std::endl;
	test_obj5.print_method_addr();
	std::cout << "==========" << std::endl;
	
	void (TestClass::*fptr) (void);
	fptr = &TestClass::test_method;
	std::cout << &fptr << std::endl;
	
	return 0;
}