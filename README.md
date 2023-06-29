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

2. After you have made a variable that is set to TensorFlow's model.fit, use the `dm.handleLogs` function. In the example below we set history to model.fit and proceed to collect log information. We then create a dataLog varible to have everything in a nice string. This will be simplified in upcoming versions.
```
history = model.fit(X_train, y_train, #this is tensorflow code that should be in your file.
                    epochs=epochs, 
                    validation_data=(X_test, y_test),
                    batch_size=batchsize,
                    callbacks=[best_cp]
)

# this is ML Doc Maker code that you will need to add to your file
train_loss = dm.handleLogs(history.history['loss'])
val_loss   = dm.handleLogs(history.history['val_loss'])
acc = dm.handleLogs(history.history['Accuracy'])
val_acc = dm.handleLogs(history.history['val_Accuracy'])

dataLog = "\n\nTrain Loss:\n"+train_loss+"\n\nVal Loss:\n"+val_loss+"\n\nAccuracy\n"+acc+"\n\nValue Accuracy:\n"+val_acc
```
