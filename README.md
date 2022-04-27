## Make a Streamlit Application

- See the [galery](https://streamlit.io/gallery?category=data-visualization).
- Follow the [initial tutorial](https://docs.streamlit.io/library/get-started).

## What we did?

1. Make a streamlit folder (work folder)
2. Download or open an IDE (VS Code, PyCharm, etc.)
3. Open work folder from step 1 with IDE
4. Open terminal in your editor, where your current working directory should be within the work folder
5. Ensure the following are installed or install.
   1. python
   2. git (optional)
   3. pipenv (pip, venv, poetry, virtualenv, etc.)
6. Create virtual environment with `pipenv shell`
7. Install `pipenv install streamlit`
8. Streamlit package installed to environment, to use streamlit package, you need to run it from the environment:
   1. `pipenv run streamlit hello`, Even tough you don't have virtualenv activated, this will run.
   2. First activate environment with `pipenv shell`, second run the streamlit with `streamlit hello` command.
9.  Launch your demo app: `streamlit hello`
10. To stop the demo app, `CTRL + C`
11. Make an empty python file. Launch it with streamlit, `streamlit run my_blank_app.py`