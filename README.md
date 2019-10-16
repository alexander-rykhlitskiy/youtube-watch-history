```bash
docker build -t youtube_history .

docker run -v $(pwd):/app -it --rm -p 8888:8888 --entrypoint=/bin/bash youtube_history
jupyter notebook

docker exec -it $(docker ps | grep youtube_history | awk '{print $1}') /bin/bash

docker run -v $(pwd):/app -it --rm youtube_history
  python main.py
  ipython nbconvert --to html stats_by_dates.ipynb
```
