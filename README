#创立一个AWS ECR (docker repository)
```
aws ecr create-repository --repository-name docker-lambda
```

#登录AWS ECR
```
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 846634201516.dkr.ecr.us-west-2.amazonaws.com
```

#在本地做docker build
```
docker build -t docker-lambda .
```

本地运行lambda
```
docker run --rm -p 8080:8080 docker-lambda
```

在本地测试lambda（在另一个terminal tab)
```
aws lambda invoke \
--region us-west-2 \
--endpoint http://localhost:8080 \
--no-sign-request \
--function-name function \
--cli-binary-format raw-in-base64-out \
--payload '{}' output.txt
```

把本地做好的容器放到AWS ECR repository
```
docker tag docker-lambda:latest 846634201516.dkr.ecr.us-west-2.amazonaws.com/docker-lambda:latest
docker push 846634201516.dkr.ecr.us-west-2.amazonaws.com/docker-lambda:latest
```
