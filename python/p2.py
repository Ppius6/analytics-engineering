import contextlib
import time

# ...existing code...


@contextlib.contextmanager
def timer():
    # nonlocal-like counter stored on the function object
    if not hasattr(timer, "_count"):
        timer._count = 0

    timer._count += 1
    start = time.perf_counter()
    try:
        yield lambda: time.perf_counter() - start  # provide a function to get elapsed time
    finally:
        # nothing to clean up here, but could print/log if desired
        pass


def fast():
    sum(i for i in range(1000))


def slow():
    time.sleep(0.1)


if __name__ == "__main__":
    with timer() as elapsed:
        fast()
    print(f"fast elapsed: {elapsed():.6f}s, timer used: {timer._count}")

    with timer() as elapsed:
        slow()
    print(f"slow elapsed: {elapsed():.6f}s, timer used: {timer._count}")
