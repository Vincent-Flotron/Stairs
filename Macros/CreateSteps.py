# CreateSteps

# doc to use it as macro: https://wiki.freecad.org/Macros/fr

def padd(nb, nbDigits):

    nbStr = str(nb)
    lenNbStr = len(nbStr)

    for i in range(0, nbDigits):
        if(i > lenNbStr - 1):
            nbStr = '0' + nbStr
    
    return str(nbStr)


def createAStep(bodyNumber, stepNumber, projectName, spreadsheet, stepPrefix):
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
    # getattr(App.getDocument(projectName), name).setExpression('.Placement.Base.z', u'{}.m{}'.format(spreadsheet, stepNumber))
    print(u'{}.{}{}'.format(spreadsheet, stepPrefix.lower, stepNumber))
    getattr(App.getDocument(projectName), name).setExpression('.Placement.Base.z', u'{}.{}{}'.format(spreadsheet, stepPrefix.lower(), stepNumber))

    # Rename the step
    FreeCAD.getDocument(projectName).getObject(name).Label = "{}{}_{}".format(stepPrefix.upper(), stepNumber, name)
    
    # Update view
    # App.ActiveDocument.recompute()
    FreeCAD.getDocument(projectName).recompute()
    # App.getDocument(projectName).recompute()
    print("Step {} on body {} created ;)".format(stepNumber, bodyNumber))
    

# # createAStep(nb=5, stepNumber=3, projectName='Maison', spreadsheet='Spreadsheet')
# createAStep(bodyNumber=6, stepNumber=4, projectName='Maison', spreadsheet='Spreadsheet')

def createSteps(firstStep, nbSteps, firstBody, projectName, spreadsheet, stepPrefix):

    projectName='Maison'
    spreadsheet='Spreadsheet'

    deltaStepBody = firstStep - firstBody

    for step in range(firstStep, firstStep + nbSteps):
        createAStep(bodyNumber=step-deltaStepBody, stepNumber=step, projectName=projectName, spreadsheet=spreadsheet, stepPrefix=stepPrefix)
        # print("step: {}, body: {}, delta: {}".format(step, step-deltaStepBody, deltaStepBody))


createSteps(firstStep=1, nbSteps=2, firstBody=17, projectName='Maison', spreadsheet='Spreadsheet', stepPrefix='N')
