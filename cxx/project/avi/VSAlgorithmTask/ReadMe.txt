================================================================================
    MFC库:VSAlgorithmTask项目概述
================================================================================

在应用程序向导中,将此VSAlgorithmTask应用程序
制作了。该应用程序不仅演示了MFC的基本用法,还演示了应用程序
提供创建程序的基本结构。

此文件包含组成VSAlgorithmTask应用程序的每个文件的
包含摘要说明。

VSAlgorithmTask.vcxproj
    使用应用程序向导创建的VC++项目的主项目文件。
    使用"应用程序向导"选择的
    包含有关平台,配置和项目功能的信息。

VSAlgorithmTask.vcxproj.filters
    使用应用程序向导创建的VC++项目的筛选器文件。
    此文件包含项目中文件和筛选器之间的连接信息。这样的
    连接用于显示在特定节点上以类似扩展名分组的文件。
    在IDE中使用。例如,".cpp"文件与"源文件"筛选器关联。
    有。

VSAlgorithmTask.h
    应用程序的默认头文件。其中包括与其他项目相关的
    包含标头(包括Resource.h)和CVSAlgorithmTaskApp应用程序
    声明类。

VSAlgorithmTask.cpp
    包含应用程序类CVSAlgorithmTaskApp的默认应用程序
    源文件。

VSAlgorithmTask.rc
    程序使用的所有Microsoft Windows资源的列表。
 其中存储在RES子目录中的图标,位图和光标
    包括。此文件直接从Microsoft Visual C++
    可以编辑。项目资源位于1042。

res\VSAlgorithmTask.ico
    用作应用程序图标的图标文件。此图标为
    由主资源文件VSAlgorithmTask.rc包含。

res\VSAlgorithmTask.rc2
    此文件包含在Microsoft Visual C++以外的其他工具中编辑的资源。
    包含。不能通过资源编辑器编辑的所有资源
    必须放入该文件中。

/////////////////////////////////////////////////////////////////////////////

应用程序向导将创建一个对话框类。

VSAlgorithmTaskDlg.h,VSAlgorithmTaskDlg.cpp-对话框
    此文件包含CVSAlgorithmTaskDlg类。这个类
    定义应用程序的主对话框行为。对话框中的模板包括:
    位于VSAlgorithmTask.rc中,可在Microsoft Visual C++中编辑。

/////////////////////////////////////////////////////////////////////////////

其他功能:

ActiveX控件
    支持在应用程序中使用ActiveX控件。

/////////////////////////////////////////////////////////////////////////////

其他标准文件:

StdAfx.h, StdAfx.cpp
    该文件包含预编译的头文件(PCH)VSAlgorithmTask.pch和
    用于构建预编译格式文件StdAfx.obj。

Resource.h
    定义新资源ID的标准头文件。
    在Microsoft Visual C++中读取和更新此文件。

VSAlgorithmTask.manifest
		应用程序清单文件是Windows XP中特定版本的Side-by-Side
	用于说明	组件的应用程序从属关系。加载程序将此信息
	使用	从组件缓存中加载适当的组件或仅用于应用程序
	加载	组件。应用程序清单与应用程序可执行文件
	安装在	文件夹中的外部.manifest文件,包含或以资源的形式
	可以包含在	可执行文件中。
/////////////////////////////////////////////////////////////////////////////

其他注释:

应用程序向导需要使用"TODO:"添加或自定义
表示源代码部分。

如果应用程序在共享DLL中使用MFC,请将其MFC DLL
必须重新部署。然后应用程序将操作系统的区域设置和
如果您使用其他语言,请使用相应的本地化资源MFC100XXX。DLL
必须重新部署。有关这两个主题的详细信息,请参阅
MSDN文档中的Visual C++应用程序重新部署条目
请参阅。

/////////////////////////////////////////////////////////////////////////////
