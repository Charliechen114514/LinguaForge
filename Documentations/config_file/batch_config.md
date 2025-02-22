# 配置文件说明

此配置文件的主要目的是为了方便批量文件翻译操作，确保源文档和翻译结果按指定格式和路径进行存储。在配置中，以下字段是必须指定的：

* `src_doc`：源文档路径
* `dest_lang`：目标语言
* `split_colon`：分隔符设置

其他字段可以使用默认值（不填写），对于批量文件生成，必须指定生成类型：

* `all-in-one`：将翻译文件汇总到指定的根目录。
* `insert-in`：将翻译文件生成到原文档的同级目录。

## 配置文件字段说明

### [type]

* `anatype`：指定文档类型，通常为 `doc-tree`。该字段用于指定文档的结构类型。**请不要修改这一字段**

### [document_path]

* `src_dir`：源文档所在目录路径。
* `dest_type`：请指定下面选项中的一个，否则解析时会报错
  * `all-in-one`：将翻译文件汇总到指定的根目录。
  * `insert-in`：将翻译文件生成到原文档的同级目录。
* `dest_dir`：翻译文件将会存放的目标目录。
* `check_suffix`：设置扫描的后缀名称

### [langs_settings]

* `dest_lang`：目标语言的设置，用于指定翻译结果的语言。
* `split_colon`：指定是否使用冒号分割翻译内容，通常为布尔值或字符串。

## 示例配置文件

# 配置文件示例，配置源文档和目标翻译设置

```
[type]
anatype = doc-tree

[document_path]
src_dir = /path/to/source/docs
dest_type = all-in-one
dest_dir = /path/to/destination/docs
check_suffix = md

[langs_settings]
dest_lang = en
split_colon = 。
```

在上述示例中：

* 源文档存放在 `/path/to/source/docs` 目录，这个时候当指定为all-in-one的时候，会生成在您指定的/path/to/destination/docs下
* 翻译文件的格式为 `md`，这将意味着只会收集目录下所有的md文档。
* 目标语言设置为 `en`（英语），并采用中文句号。作为分隔，从而更准确的提升翻译质量。



