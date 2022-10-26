# Only First

olf 只保留最前面的部分。

## features

- [x] 将代码只保留前面的一部分；
- [ ] 将 Django models 代码转换成样例数据；
- [ ] 将样例数据转换成 Django models

## Install

`pip install onlyfirst`

## Usage

In file `temp.txt`:

```txt
main = 'test',
hello = 'world',
why = 'true'
```


Run: `onlyfirst temp.txt`

```txt
main =
hello =
why =
```

