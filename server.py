# A Flask based web application that receives data, executes a series of instructions, and returns the result
from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import pandas as pd

# Create the Flask app instance
app = Flask(__name__)
CORS(app)

# Connect to the database and read data into a Pandas dataframe
con = sqlite3.connect("database/cia.db")
dfOriginal = pd.read_sql("SELECT * FROM cia", con)
dfOriginal.columns = ["LID", "Name", "Region", "Flaeche", "Einwohner", "BIP"]



# A function to execute a list of instructions using exec function
def executePOST(userList):
    result = {}
    for instructions in userList:
        exec(instructions)
    return result['df']

# A function to modify the userList
def modifyUserList(userList):
    helpList = ["df = dfOriginal.copy()", "result['df'] = df"]
    userList.insert(0, helpList[0])
    userList.append(helpList[1])
    return userList


# Route to receive and process data
@app.route('/lectionOne/2', methods=['POST'])
def lectureOne_2():
    response = {"success": None, "result": {}, "errorMessage" : None}

    # Result of lecture
    dfResult = dfOriginal.copy()
    dfResult = dfResult["Name"]
    
    # Prepare the list of instructions to be executed
    userList = list(request.json)
    userList = modifyUserList(userList)
       
    # Execute the instructions and save the result in dfUser
    dfUser = executePOST(userList)
    dfUserJSON = dfUser.to_json()
  
    # Compare the result with the original data
    try:
        if dfResult.equals(dfUser):
            response["success"] = True
            response["result"] = dfUserJSON
        else:
            response["success"] = False
            
        return jsonify(response)
    except Exception as e:
        response["errorMessage"] = str(e)
        return jsonify(response)

# Route to receive and process data
@app.route('/lectionOne/3', methods=['POST'])
def lectureOne_3():
    response = {"success": None, "result": {}, "errorMessage" : None}

    # Result of lecture
    dfResult = dfOriginal.copy()
    dfResult = dfResult[['Name','Einwohner']][ dfResult['Einwohner'] > 1E08 ]
    
    # Prepare the list of instructions to be executed
    userList = list(request.json)
    userList = modifyUserList(userList)

   
    # Execute the instructions and save the result in dfUser
    dfUser = executePOST(userList)
    dfUserJSON = dfUser.to_json()
  
    # Compare the result with the original data
    try:
        if dfResult.equals(dfUser):
            response["success"] = True
            response["result"] = dfUserJSON
        else:
            response["success"] = False
            
        return jsonify(response)
    except Exception as e:
        response["errorMessage"] = str(e)
        return jsonify(response)

# Route to receive and process data
@app.route('/lectionOne/4', methods=['POST'])
def lectureOne_4():
    response = {"success": None, "tips": None, "errorMessage" : None}

    # Result of lecture
    dfResult = dfOriginal.copy()
    dfResult = dfResult['Name'][ dfResult['BIP'].between(1E9,100E9) ]
    
    # Prepare the list of instructions to be executed
    userList = list(request.json)
    userList = modifyUserList(userList)
   
    # Execute the instructions and save the result in dfUser
    dfUser = executePOST(userList)
    
    # Compare the result with the original data
    try:
        if dfResult.equals(dfUser):
            response["success"] = True
        else:
            response["success"] = False
        return jsonify(response)
    except Exception as e:
        response["errorMessage"] = str(e)
        return jsonify(response)
    
# Route to receive and process data
@app.route('/lectionOne/5', methods=['POST'])
def lectureOne_5():
    response = {"success": None, "result": {}, "errorMessage" : None}

    # Result of lecture
    dfResult = dfOriginal.copy()
    dfResult = dfResult[['Name','Einwohner']][ dfResult['Name'].str.contains('Frankreich|Deutschland|Polen', regex=True) ]
    
    # Prepare the list of instructions to be executed
    userList = list(request.json)
    userList = modifyUserList(userList)
   
    # Execute the instructions and save the result in dfUser
    dfUser = executePOST(userList)
    dfUserJSON = dfUser.to_json()

    # Compare the result with the original data
    try:
        if dfResult.equals(dfUser):
            response["success"] = True
            response["result"] = dfUserJSON
        else:
            response["success"] = False
            
        return jsonify(response)
    except Exception as e:
        response["errorMessage"] = str(e)
        return jsonify(response)

# Route to receive and process data
@app.route('/lectionOne/6', methods=['POST'])
def lectureOne_6():
    response = {"success": None, "result": {}, "errorMessage" : None}

    # Result of lecture
    dfResult = dfOriginal.copy()
    dfResult['Einwohner in Mio'] = (dfResult['Einwohner']/1E6).round(2)
    dfResult = dfResult[['Name', 'Einwohner in Mio']] [ dfResult['Region'] == 'Südamerika' ]
    

    # Prepare the list of instructions to be executed
    userList = list(request.json)
    userList = modifyUserList(userList)

    # Execute the instructions and save the result in dfUser
    dfUser = executePOST(userList)
    dfUserJSON = dfUser.to_json()

    # Compare the result with the original data
    try:
        if dfResult.equals(dfUser):
            response["success"] = True
            response["result"] = dfUserJSON
        else:
            response["success"] = False
            
        return jsonify(response)
    except Exception as e:
        response["errorMessage"] = str(e)
        return jsonify(response)

# Route to receive and process data
@app.route('/lectionOne/7', methods=['POST'])
def lectureOne_7():
    response = {"success": None, "result": {}, "errorMessage" : None}

    # Result of lecture
    dfResult = dfOriginal.copy()
    dfResult['pro Kopf-Jahreseinkommen'] = (dfResult['BIP']/dfResult['Einwohner']).round(2)
    dfResult = dfResult[['Name','pro Kopf-Jahreseinkommen']] [ dfResult['Einwohner'] > 200E6 ]
    
    # Prepare the list of instructions to be executed
    userList = list(request.json)
    userList = modifyUserList(userList)
    print(userList)
   
    # Execute the instructions and save the result in dfUser
    dfUser = executePOST(userList)
    dfUserJSON = dfUser.to_json()

    # Compare the result with the original data
    try:
        if dfResult.equals(dfUser):
            response["success"] = True
            response["result"] = dfUserJSON
        else:
            response["success"] = False
            
        return jsonify(response)
    except Exception as e:
        response["errorMessage"] = str(e)
        return jsonify(response)

# Route to receive and process data
@app.route('/lectionOne/8', methods=['POST'])
def lectureOne_8():
    response = {"success": None, "result": {}, "errorMessage" : None}

    # Result of lecture
    dfResult = dfOriginal.copy()
    dfResult['pro Kopf-Jahreseinkommen'] = (dfResult['BIP']/dfResult['Einwohner']).round(2)
    dfResult[['Name','pro Kopf-Jahreseinkommen']] [ dfResult['Einwohner'] > 200E6 ].sort_values(by='pro Kopf-Jahreseinkommen')

    # Prepare the list of instructions to be executed
    userList = list(request.json)
    userList = modifyUserList(userList)
   
    # Execute the instructions and save the result in dfUser
    dfUser = executePOST(userList)
    dfUserJSON = dfUser.to_json()

    # Compare the result with the original data
    try:
        if dfResult.equals(dfUser):
            response["success"] = True
            response["result"] = dfUserJSON
        else:
            response["success"] = False
            
        return jsonify(response)
    except Exception as e:
        response["errorMessage"] = str(e)
        return jsonify(response)

# Route to receive and process data
@app.route('/lectionOne/9', methods=['POST'])
def lectureOne_9():
    response = {"success": None, "result": {}, "errorMessage" : None}

    # Result of lecture
    dfResult = dfOriginal.copy()
    dfResult = dfResult[ dfResult['Name'].str.contains("Vereinigte", regex=True) ]
    
    # Prepare the list of instructions to be executed
    userList = list(request.json)
    userList = modifyUserList(userList)

    # Execute the instructions and save the result in dfUser
    dfUser = executePOST(userList)
    dfUserJSON = dfUser.to_json()

    # Compare the result with the original data
    try:
        if dfResult.equals(dfUser):
            response["success"] = True
            response["result"] = dfUserJSON
        else:
            response["success"] = False
            
        return jsonify(response)
    except Exception as e:
        response["errorMessage"] = str(e)
        return jsonify(response)

# Route to receive and process data
@app.route('/lectionOne/10', methods=['POST'])
def lectureOne_10():
    response = {"success": None, "result": {}, "errorMessage" : None}

    # Result of lecture
    dfResult = dfOriginal.copy()
    dfResult = dfResult['Region']
    dfResult = pd.unique(dfResult)
    dfResult.sort()
    
    # Prepare the list of instructions to be executed
    userList = list(request.json)
    userList = modifyUserList(userList)
    
   
    # Execute the instructions and save the result in dfUser
    dfUser = executePOST(userList)
    #dfUserJSON = dfUser.to_json()
   
    # Compare the result with the original data
    try:
        if all(x == y for x, y in zip(dfResult, dfUser)):
            response["success"] = True
            #response["result"] = dfUserJSON
        else:
            response["success"] = False
        return jsonify(response)
    except Exception as e:
        response["errorMessage"] = str(e)
        return jsonify(response)

# Route to receive and process data
@app.route('/lectionOne/11', methods=['POST'])
def lectureOne_11():
    response = {"success": None, "result": {}, "errorMessage" : None}

    # Result of lecture
    dfResult = dfOriginal.copy()
    dfResult = dfResult["Name"]
    
    # Prepare the list of instructions to be executed
    userList = list(request.json)
    userList = modifyUserList(userList)

   
    # Execute the instructions and save the result in dfUser
    dfUser = executePOST(userList)
    dfUserJSON = dfUser.to_json()

    # Compare the result with the original data
    try:
        if dfResult.equals(dfUser):
            response["success"] = True
            response["result"] = dfUserJSON
        else:
            response["success"] = False
            
        return jsonify(response)
    except Exception as e:
        response["errorMessage"] = str(e)
        return jsonify(response)







# Start the Flask app
if __name__ == "__main__":
    app.run()
