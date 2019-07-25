```C++
#include <iostream>
class Singleton
{
public:
    ~Singleton() {}
    static Singleton & getInstance()
    {
        static Singleton instance;
        return instance;
    }
    void print()
    {
        std::cout << "print test" << std::endl;
    }
private：
	Singleton(){}
};

int main()
{
	Singleton::getInstance().print();
}
```
