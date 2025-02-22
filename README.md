# LinguaForge

> 前言：所有的除中文文档以外的所有文档都是本项目LinguaForge生成的（笑

# README

![(Language)](https://img.shields.io/badge/language-python>=3.12-brightgreen)![STILL_IN_MAINTAINS](https://img.shields.io/badge/Maintains-YES-red)![License](https://img.shields.io/badge/license-GNUv3-yellow)  ![Documentation](https://img.shields.io/badge/documentation-on_the_way-brightgreen)![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen)

![GUI](https://img.shields.io/badge/Language-Select_One!-green)

[简体中文](./README.md)

[English](./README_en.md)

![GUI](https://img.shields.io/badge/Introduction-LinguaForge-blue)

​	LinguaForge是一个批量文档翻译的生成器，希望助力于给定的文档树结构的批量翻译处理。当前的分支是CLI命令行分支。

![GUI](https://img.shields.io/badge/Usage-How_To_Install_LinguaForge-red)

#### 如果你此前没有安装过poetry

​	本项目使用Poetry管理我们的依赖，在任何一个Python虚拟环境中，请你先安装Poetry，关于Poetry的安装请参考：

> [Introduction | Documentation | Poetry - Python dependency management and packaging made easy](https://python-poetry.org/docs/#installation)

​	或者你可以直接使用命令

```
pip install poetry
```

#### 安装项目

​	安装项目在Poetry下非常的简单，当克隆好仓库并进入本项目的根目录后，只需要

```
poetry install
```

​	等待依赖安装完毕后就可以欢乐的使用了！



![GUI](https://img.shields.io/badge/Usage-How_To_Use_LinguaForge-blue)

在部署结束LinguaForge之后，你只需要在命令行中输入：

```
python -m linguaforge.main "commands"
```

​	其中，commands的值可以是如下的这些值

1. **single-doc**
   通过命令行交互式进行对单个文件的翻译。
2. **single-doc-from-config**
   根据给定的配置文件进行单个文件的翻译。
3. **batch-doc-from-config**
   根据配置文件进行批量文件的翻译。此命令用于批量处理多个翻译文件。
4. **remove-trans**
   通过给定的历史文件记录删除翻译。当你之前进行过翻译时会询问你是否需要此类文件。需要删除给定的某次翻译的结果时，可以使用此命令。
5. **gen-sf-config**
   生成单文件翻译配置模板。该模板可以用于构建新的单文件翻译配置。
6. **gen-bd-config**
   生成批量文档翻译配置模板。该命令用于批量处理多个文档的翻译配置。
7. **langs-list**
   检查默认语言支持的语言列表。该命令可以帮助你确认哪些语言被支持进行翻译。
8. **format-file-list**
   查看支持的文件格式配置类型列表。此命令展示支持的文件类型，适用于翻译配置。

​	如果你还有更多的问题，请键入

```
python -m linguaforge.main --help
```

![Documentation](https://img.shields.io/badge/documentation-on_the_way-brightgreen)

​	关于配置文件的事情，你的确需要前往[文档](./Documentations)下看看。里面有多语言的说明，选择你喜欢的那个 :)
