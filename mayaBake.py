import maya.cmds as cmds

def SmoothNormalsToVxColor():
    objList = cmds.ls(sl=True, o=True) #get all selected Objects

    for obj in objList:

        shape = cmds.listRelatives(obj, s=True)[0] #get first shape of selected Objects
        ob = cmds.duplicate(obj)
        ob = ob[0]

        cmds.polySoftEdge(ob, a=180)

        normals = []
        objVertices = []
        vertCount = cmds.polyEvaluate(ob, v=True)

        for vert in range(vertCount):
            vertex = "%s.vtx[%s]" %(ob, vert)
            objVertices.append("%s.vtx[%s]" %(obj, vert))
            normal = cmds.polyNormalPerVertex(vertex, query=True, xyz=True)
            normals.append([vertex, normal])

        print(normals)

        for n in range(len(normals)):
            cmds.select(normals[n][0]) #select the vertex name of n

            r = normals[n][1][0]/2+0.5
            g = normals[n][1][1]/2+0.5
            b = normals[n][1][2]/2+0.5

            cmds.select(objVertices[n])
            cmds.polyColorPerVertex(rgb = (r,g,b))
            cmds.setAttr("%s.displayColors" % shape,1)


        cmds.delete(ob)

SmoothNormalsToVxColor()