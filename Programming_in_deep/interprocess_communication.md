현대의 OS는 프로세스가 메모리에 직접 접근하는 것을 허용하지 않는다.

이 차단은 2가지 방식으로 구성되어 있는데, 하나는 가상화Memory Virtualization이고, 다른 하나는 다른 프로세스의 메모리에 대한 차단이다.

이 중 가상화는 프로세스가 사용하는 메모리의 주소 정보를 통해 실제 메모리 상의 주소를 찾아낼 수 없도록 하는 것이고(MMU - memory management unit), 다른 프로세스의 메모리에 대한 차단은 권한이 없는 프로세스가 다른 프로세스의 메모리를 통해 정보를 탈취하거나, 행동을 조작하는 것을 막기 위함이다. 다른 프로세스의 메모리에 접근할 수 없는 것은 모든 프로세스가 해당하는 것은 아니고, 관리자에 준하는 권한이 있다면 다른 프로세스의 메모리를 읽을 수 있고, 이는 디버깅, reverse engineering 등에 활용된다.

아무튼, 보안을 위해 프로세스간 메모리에 대한 접근은 차단되어 있기에 프로세스간 정보를 공유하는 행위는 굉장히 많은 제한을 받는다.

이를 해결하기 위한 방법은 다음과 같다.
    1. Pipe를 사용한다.
        - 파이프는 OS의 Kernel에서 제공하는 one-directional한 read/write 페어다. 내부적으로야 shared_memory든 뭐든 구현되어 있겠지만 그건 정확하게 모르겠다.
    2. socket을 사용한다. 
        - (Linux) Unix domain socket을 이용하여 통신한다.
        - loopback을 이용해 socket으로 데이터를 주고 받는다.
    3. Shared memory를 사용한다.
        - c- shmget
        - https://en.wikipedia.org/wiki/Shared_memory
    4. remote call protocol을 사용한다.
        - 실시간은 아니고, DBUS 등을 이용해서 다른 프로세스에서 원하는 동작이 실행되도록 하는 것
