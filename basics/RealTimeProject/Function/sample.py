def ready():
    print("Im drinking my coffee")

call = lambda x : (
    print("Your Coffee is ready"),
    x()
)
call(ready)