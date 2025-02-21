# Operating system hand rub tutorial starting from 0

​ Start writing at 12 noon on February 10, 2025.

## Preface

​ In October 2023, as a sophomore, I first came into contact with the operating system course. At that time, I had just learned the OS Lab of MIT (the experiment was not completed, and I didn’t do it until the beginning of 2025. Completed the work I should have done), and at the same time, I also started my first high-difficulty project, which is to rub out a running, simplest operating system from a blank article come out!

​ In fact, there are many excellent operating system tutorials, and I am very willing to give some examples here!

> [SamyPesse/How-to-Make-a-Computer-Operating-System: How to Make a Computer Operating System in C++ (github.com)](https://github.com/SamyPesse/How-to-Make- a-Computer-Operating-System)
>
> [Cooi-Boi/Tiny-OS: "Operating System Truth Restore" implements self-write source code and records the entire implementation process of the operating system in detail on CSDN, including Debug steps and error errata in the book Bochs2.6.8 Gcc4.4 Except for the last of this book All three small functions and the rest implement about 6k lines of code. I hope it can help you ^^ (github.com)](https://github.com/Cooi-Boi/Tiny-OS)

However, the author noticed that the tool chains they used were so old that when I mustered up the courage to take a look at the tool chains they used, I found that they were basically outdated for more than ten years. The codes used in these tutorials that are modified are either serial errors or stuck in the relay of the mode, and novices have no idea what is going on. I had to leave in depression, or some people like me were willing to turn back on the old toolchain they used. As it turns out, it will only mess up your environment in the end. When I wrote it, I tested three groups of operating system environments.

- WSL (Windows Subsystem For Linux) (Arch WSL and Typical Ubuntu WSL have been tested),
- Ubuntu24.04,
- Arch Linux

​ Both can configure the target environment correctly (Arch is a bit more difficult, we have to work hard to compile gcc4.4 and bochs, and it will end up being messy)

Now as a preface, I will briefly explain what you need to do before you start:

1. Be patient, I am also a novice in the operating system! I also encountered problems that were very frustrating when I rubbed my hands before, but I persisted and finally got through a difficult month to eliminate the problem. They may be - writing the wrong configuration, copying the wrong code, putting our stuff in a position that should not be placed, setting the wrong link order leads to illegal address access... Please, any one can make us headache No more! However, these authors believe are a necessary test for becoming a qualified programmer - we need to develop a ability to solve the problems we encounter in an environment of limited information.
2. Learn to find information! It would be meaningless if it wasn't for being closed to the country. What we need is to find manuals, find blogs written by others, compare other people's methods, and force ourselves to learn new technologies to solve the problems we encounter. Instead of copying other people's solutions completely. Taking "Operating System Restores the Truth" as an example, there are still many people posting their blogs almost entirely original, without any thoughts on how to transfer other people's output. This is not good! It does not help improve your abilities!
3. Try new tools. The author also read the documents of gcc and bochs, carefully read every communication, hoping that when I click on the next page, or scroll my mouse wheel, I can finally see the answer I have been looking forward to. All right! It was still very difficult. When I solved it, I basically went all night until three o'clock every day, or got up at midnight at 5 o'clock in the morning to continue my research. Of course, you don’t need to do this by reading the blog I wrote here. It’s better to laugh at me after tea and blow water (laughing)
4. Make sure your computer can run virtual machines! What I must explain is that because the content I learn is classic and my level is even more scattered, ** can only write a 32-bit operating system instead of a 64-bit operating system. There is not much time to really take root in the `Intel/AMD` architecture manual that is tens of thousands of pages small to find answers page by page. So, I want to apologize for my own slackness! To this end, the author uses a bochs virtual machine (note that it is non-GDB debugging), which is relatively convenient for our debugging. At least, the Makefile given by me is all debugging mode by default, which is convenient for us to control and observe the behavior and phenomena of the operating system. Of course, interested friends can naturally try to use bochs-with-gdb, but as of now, the author's focus is still on implementing this operating system and completing as many functions as possible. So, please spare no effort Friends try it on their own. If possible, they are willing to share their work. Send it to me an Issue or PR (Pull Request) at any time. I will check your work as soon as possible!

## So, I...

Now, when you make up your mind instead of giving up and close the browser tag interface, then cheer yourself up, which means you are willing to take action and start your operating system hand rub journey!

​ The author now gives these setup configurations. Please complete your configuration work as needed! At this point, my thoughts have been completed! Good luck!

> Next: See the [setups](./setups/README.md)!
>
> Or english version: [setup](./setups/README_EN.md)