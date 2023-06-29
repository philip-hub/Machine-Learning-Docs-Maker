# Machine-Learning-Docs-Maker

This package can be used with TensorFlow and MatPlot Lib to save documention on TensorFlow Machine Learning Models Performance.

# Setup
1. Download main.py
2. Rename it to document_models.py (optional)
3. Use what you named it and import it as dm <br>
`import document_models as dm`
4. The package will automacticaly setup and create two new folders called "model_documentation" and  "doc_model_setup." These can be changed in the top of the main file if they are conflicting.

# Usage

1. Anywhere in your notebook before running any of the other functions in this package put in the line <br>
    `osWritePath, fileHead = dm.docSetup("")`
This will create the path and title for the document. You can pass a string into the function for a custom name otherwise it will be test #n with n being the number of times it was ran. The defualt should be prefered if you need to run a lot of tests and save a lot of results.

2. 
