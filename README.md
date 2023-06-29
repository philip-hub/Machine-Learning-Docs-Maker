# Machine-Learning-Docs-Maker

Build In | Contributors | Live version | Current Realease
--- | --- | --- | ---
**Python 🐍** | [@philip-hub](https://github.com/philip-hub) | Here | Beta

![just for fun](https://media4.giphy.com/media/MKorKFj0Muz4P0CI7D/giphy.gif?cid=ecf05e47o5eob94tjfen8iu5w95jekxx1co44buhwcbtw8tw&ep=v1_gifs_search&rid=giphy.gif&ct=g)
This package can be used with TensorFlow and MatPlot Lib to save documention on TensorFlow Machine Learning Models Performance.

# Setup
1. Download main.py
2. Rename it to document_models.py (optional)
3. Use what you named it and import it as dm <br>
```
import document_models as dm
```
Also it is assumed you are importing TensorFlow and matplotlib
```
import tensorflow as tf
import matplotlib.pyplot as plt
```

5. The package will automacticaly setup and create two new folders called "model_documentation" and  "doc_model_setup." These can be changed in the top of the main file if they are conflicting.

# Usage

1. Anywhere in your notebook before running any of the other functions in this package put in the line <br>
    ```
   osWritePath, fileHead = dm.docSetup("")
    ```
    This will create the path and title for the document. You can pass a string into the function for a custom name otherwise it will be test #n with n being the number of times it was       ran. The defualt should be prefered if you need to run a lot of tests and save a lot of results.

2. It is reccomended that you do not hard code hyperparemeters in your tensor flow file instead put th near the top of your file and use them as varibles. For ML Doc Maker you will need to create 2 lists one list with the hyperparameters names and spec names about the model and another list with the hyperparameters values and model spec values. Order needs to corespond in both lists. This will be simiplified to a dictionary in a later release. Here is an example:
```
seed = 42 #general specs about the model
testSize = .2
act_function = "sigmoid"
optimizier = "Adam" # only to document this has to be changed in the cell 13 

#hyperparameters
lstm_units = 50
lr = 5e-4
batchsize = 16
epochs = 50

#required for ML Doc Maker
hyper_params = ["Random Seed","Test Split","Activation","Optimizer","LSTM Units","Learning Rate", "Batchsize", "Epochs"]
hyper_params_values = [seed, testSize, act_function, optimizier, lstm_units,lr,batchsize,epochs]

```


3. After you have made a variable that is set to TensorFlow's model.fit, use the `dm.handleLogs` function. In the example below we set history to model.fit and proceed to collect log information. We then create a dataLog varible to have everything in a nice string. This will be simplified in upcoming versions.
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
4. Next for your plots use the Matplot lib to create and save them. Save them using the osPath varible made above plus the desired file name. Then append the file names to a list. T Examples below.
```
# creating the plot matplot lib
plt.plot(history.history['loss'], 'o--', label="Train")
plt.plot(history.history['val_loss'], 'o--', label="Val")
plt.ylim(0.0,10)
plt.legend()

#showing the plot
acc_plot = plt.gcf()
plt.show()
plt.draw()

#saving the plot and adding it to a list called plotFiles
fileName = "lossplot.jpg"
plotPath = osWritePath+fileName
acc_plot.savefig(plotPath)
plotFiles = [fileName]

#repeating the process
plt.plot(history.history['Accuracy'], 'o--', label="Accuracy")
plt.plot(history.history['val_Accuracy'], 'o--', label="Val_Accuracy")
plt.ylim(0.0,1)
plt.legend()

acc_plot = plt.gcf()
plt.show()
plt.draw

fileName2 = "accplot.jpg"
plothPath = osWritePath+fileName2
acc_plot.savefig(plotPath)
plotFiles.append(fileName2)
```
5. Run this function using all the parameters we made above.

```
dm.docModel(fileHead, hyper_params, hyper_params_values, plotFiles, dataLog, osWritePath)
```
   It will then create new Markdown (.md) file inside the folder that is set to Test #n. The markdown will look similar to this <a href="https://github.com/philip-hub/Machine-Learning-Docs-Maker/blob/main/Test%20Example/model_documentation.md">example</a>.
