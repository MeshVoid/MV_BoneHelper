# MV_RigHelper_

**MeshVoid's Rigging Helper Addon For Blender**

An addon to ease the burden of a process of manual rigging in Blender



#### **General rigging workflow tips**

**Naming conventions**

Naming convention includes Prefixes such as:

 DEF_ DEF. 

TGT. TGT_ 

CTL. CTL_ (alt. CTRL, CON) 

MCH. MCH_  

IK. IK_ 

FK. FK 

and additional abbreviations include: ORG. ORG_ 

*Bone types:*     

- ROOT (Single main bone to tie the whole armature together)

- Deformation bones (with deform property turned on)

- Target bones (Bones that are constrained to deformation bones via transform constraints)

- Control bones (Bones that are constrained to target bones and control them )

- Mechanism bones (Helper bones that help glue together mechanism of constraints)

- ORG - Original bones from a different armature (might be an exported armature)

WGT - widgets (geometrical custom shapes for selected bones)



**Stages of rigging:**

- Create Deformation Armature Bone hierarchy with proper naming convention and prefixes (One side is enough)

- Duplicate The created bone hierarchy rename prefixes of bones from DEF to TGT and get rid of .001 suffix, make sure that TGT don't have 'deform' properties

- 

Biped rigging tips:



Leg rigging (Reverse foot rig mechanism)

**Leg naming convention**



DEF layer:

DEF.

DEF.Thigh.L/R

DEF.Shin.L/R



## **Initial TODO's for addon:**



- [ ] Write an operator that duplicates and renames the deformation bones with DEF. DEF_ prefixes to TGT. TGT__ and then applies transform constraints to newly created target bones to copy DEF transformation values (also set 'deform' property of TGT bones to False)

- [ ] 

- [ ] 


