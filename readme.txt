读取某个xml文件，例如“cutter_zh.ts”，当里面translation节点的type属性是obsolete时，删除整个translation字节和其父节点。
若translation字节的父节点的父节点（即context节点），没有message字节时，删除context节点。再删除多余空行。