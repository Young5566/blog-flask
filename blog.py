from app import create_app


run = create_app('default')


if __name__ == '__main__':
    run.run('0.0.0.0')
