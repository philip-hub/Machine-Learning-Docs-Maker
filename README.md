# Machine-Learning-Docs-Maker

This package can be used with TensorFlow and MatPlot Lib to save documention on TensorFlow Machine Learning Models Performance.

# Setup
1. Download main.py
2. Rename it to document_models.py (optional)
3. Use what you named it and import it as dm <br>
`import document_models as dm`
4. The package will automacticaly setup and create two new folders called "model_documentation" and  "doc_model_setup." These can be changed in the top of the main file if they are conflicting.

# Usage

1. Anywhere in your notebook before running any of the other packages put in the line <br>
    `osWritePath, fileHead = dm.docSetup("")`
