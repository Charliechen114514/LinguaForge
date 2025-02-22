# 配置文件说明

这是单文档翻译配置文件。以下字段是必须指定的：

- `src_doc`：源文档路径
- `dest_lang`：目标语言
- `split_colon`：分隔符设置

其他字段将使用默认值。

## 配置文件字段说明

### [type]

- `anatype`：指定文档类型，必须设置为 `single-file`，表示单个文档翻译。

### [document_path]

- `src_doc`：源文档路径。该字段指定需要翻译的源文档位置。
- `dest_doc`：目标文档路径。该字段指定翻译后的文档存储位置。

### [langs_settings]

- `dest_lang`：目标语言。此字段指定翻译文档的目标语言。
- `split_colon`：分隔符设置。指定是否使用冒号作为翻译内容的分隔符。通常为布尔值或字符串。

## 示例配置文件

```
[type]
anatype = single-file

[document_path]
src_doc = /path/to/source/document.txt
dest_doc = /path/to/destination/translated_document.txt

[langs_settings]
dest_lang = en
split_colon = 。
```

在上述示例中：

- 源文档 `/path/to/source/document.txt` 将被翻译。
- 翻译后的文档将保存为 `/path/to/destination/translated_document.txt`。
- 翻译目标语言为 `en`（英语），并采取中文的句号。作为分隔符