# CreateSteps

def padd(nb, nbDigits):

    nbStr = str(nb)
    lenNbStr = len(nbStr)

    for i in range(0, nbDigits):
        if(i > lenNbStr - 1):
            nbStr = '0' + nbStr
    
    return str(nbStr)


def createAStep(bodyNumber, stepNumber, projectName, spreadsheet):
    # Create the step
    ### Begin command PartDesign_Body
    name = 'Body' + padd(bodyNumber, 3)
    print(name)
    App.activeDocument().addObject('PartDesign::Body', name)
    Gui.activateView('Gui::View3DInventor', True)
    Gui.activeView().setActiveObject('pdbody', getattr(App.activeDocument(), name))
    Gui.Selection.clearSelection()
    Gui.Selection.addSelection(getattr(App.ActiveDocument, name))
    App.ActiveDocument.recompute()
    ### End command PartDesign_Body
    
    # Place the step in z axis
    getattr(App.getDocument(projectName), name).setExpression('.Placement.Base.z', u'{}.m{}'.format(spreadsheet, stepNumber))

    # Rename the step
    FreeCAD.getDocument(projectName).getObject(name).Label = "M{}_{}".format(stepNumber, name)
    
    # Update view
    # App.ActiveDocument.recompute()
    FreeCAD.getDocument(projectName).recompute()
    # App.getDocument(projectName).recompute()
    print("Step {} on body {} created ;)".format(stepNumber, bodyNumber))
    

# # createAStep(nb=5, stepNumber=3, projectName='Maison', spreadsheet='Spreadsheet')
# createAStep(bodyNumber=6, stepNumber=4, projectName='Maison', spreadsheet='Spreadsheet')

def createSteps(firstStep, nbSteps, firstBody, projectName, spreadsheet):

    nbSteps = 14 - 4
    firstBody = 7
    firstStep = 5
    projectName='Maison'
    spreadsheet='Spreadsheet'

    deltaStepBody = firstStep - firstBody

    for step in range(firstStep, firstStep + nbSteps):
        createAStep(bodyNumber=step-deltaStepBody, stepNumber=step, projectName=projectName, spreadsheet=spreadsheet)
        # print("step: {}, body: {}, delta: {}".format(step, step-deltaStepBody, deltaStepBody))


createSteps(firstStep=5, nbSteps=14-4, firstBody=7, projectName='Maison', spreadsheet='Spreadsheet')