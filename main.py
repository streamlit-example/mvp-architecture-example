from streamlit import session_state as stss

from presenter.presenter import Presenter


def main():
    if "presenter" not in stss:
        stss.presenter = Presenter()
    stss.presenter.run()


if __name__ == "__main__":
    main()
