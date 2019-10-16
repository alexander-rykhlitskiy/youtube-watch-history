```bash
docker build -t youtube_history .
docker run -v $(pwd):/app -it --rm --entrypoint=/bin/bash youtube_history
docker run -v $(pwd):/app -it --rm youtube_history python main.py
```
