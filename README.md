
# jaeger


### 配置完成之后, 浏览器header中没有增加trace_id 头部信息

  到django_opentracing  lib中找到tracing.py文件
  定位到131行左右增加下面行，重启项目，在header会自动添加进来.

  ```
  132:  if response is not None:
  133:     scope.span.set_tag(tags.HTTP_STATUS_CODE, response.status_code)
  134:     response["trace-Id"] = format(scope.span.trace_id, "x")   # 增加此行

  ```
