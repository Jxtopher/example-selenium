# Use case selenium

```bash
docker build . -t chromiun
docker run --rm --name devtest --mount type=bind,source="$(pwd)"/results,target=/home/user/results chromiun:latest
```