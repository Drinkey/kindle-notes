# kindle-notes

Python scripts to convert Kindle exported notes to Markdown

## Environment

Python3.6

To install dependencies

```bash
$ git clone https://github.com/Drinkey/kindle-notes.git
$ cd kindle-notes
$ make init
```

## Usage examples

A simple exported HTML doc from Kindle for Android

```
$ python kindle-notes/kindle-notes.py --html tests/samples/奈飞文化手册-Notebook.html 
Loading <class: KindleNotesHtml_1_21> from <module: utils.html.v_1_21>
# 奈飞文化手册

> 【美】帕蒂.麦考德（Patty McCord）; 范珂译

# 01 文化准则1 我们只招成年人

> 伟大的团队是这样的团队：其中的每一位成员都知道自己要前往何方，并愿意为此付出任何努力。建立伟大的团队不需要靠激励、程序和福利待遇，靠的是招聘成年人，渴望接受挑战的成年人，然后，清晰而持续地与他们沟通他们面对的挑战是什么。

## 成年人最渴望的奖励，就是成功

> 成年人最渴望的奖励，就是成功

# 02 文化准则2 要让每个人都理解公司业务

> 标。”管理者越是花更多的时间去详尽、透彻地沟通亟待完成的工作任务、面临的挑战以及竞争环境，那些政策、审批和激励措施就越不重要。

## 培养基层员工的高层视角

> 员工需要以高层管理者的视角看事物，以便感受到自己与所有层级、所有部门都必须解决的问题有真正的联系，这样公司才能发现每个环节上的问题和机会，并采取有效行动。

```

For English, must specify `--lang en`, otherwise, spaces between words will be removed, will improve this later.

```
python kindle-notes/kindle-notes.py --html tests/samples/Clean\ Architecture:\ A\ Craftsman\'s\ Guide\ to\ Softwar\ -\ 笔记本.html --lang en
Loading <class: KindleNotesHtml_1_21> from <module: utils.html.v_1_21>
# Clean Architecture: A Craftsman's Guide to Software Structure and Design (Robert C. Martin Series)

> Robert C. Martin

# The Goal?

> The goal of software architecture is to minimize the human resources required to build and maintain the required system. The measure of design quality is simply the measure of the effort required to meet the needs of the customer. If that effort is low, and stays low throughout the lifetime of the system, the design is good. If that effort grows with each new release, the design is bad. It’s as simple as that.

# Case Study

> These developers buy into a familiar lie: “We can clean it up later; we just have to get to market first!” Of course, things never do get cleaned up later, because market pressures never abate. Getting to market first simply means that you’ve now got a horde of competitors on your tail, and you have to stay ahead of them by running as fast as you can.

> The bigger lie that developers buy into is the notion that writing messy code makes them go fast in the short term, and just slows them down in the long term. Developers who accept this lie exhibit the hare’s overconfidence in their ability to switch modes from making messes to cleaning up messes sometime in the future, but they also make a simple error of fact. The fact is that making messes is always slower than staying clean, no matter which time scale you are using.

> The only way to go fast, is to go well.

# Encapsulation?

> The reason encapsulation is cited as part of the definition of OO is that OO languages provide easy and effective encapsulation of data and function.

# Chapter 7 SRP: The Single Responsibility Principle

> Of all the SOLID principles, the Single Responsibility Principle (SRP) might be the least well understood.
```

# Notes
The latest Kindle for Mac (1.25.2) has some problem in exported HTML document, the structure is wrong. Contacting with customer support to fix the problem. The default parser (1.21) still works for most of the documents.