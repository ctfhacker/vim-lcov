# vim-lcov

vim plugin to show covered and uncovered coverage lines by lcov info file

## Example lcov file

```
TN:
SF:/tmp/covtest/main.c
DA:1,0
DA:2,0
DA:3,0
DA:5,0
DA:7,1
DA:8,1
DA:9,0
DA:10,0
DA:11,0
DA:12,0
DA:13,0
DA:17,1
DA:18,1
end_of_record
```

## how to use

```
:LcovVisible <filepath of .info file>
```

If you set `VIM_LCOV_INFO_FILEPATH` environment variable, this plugin load info file automatically.

``` bash
export VIM_LCOV_INFO_FILEPATH=coverage.info
vim main.cpp
```
