from deepface import DeepFace

def detect_faces(frame):
    faces = DeepFace.extract_faces(frame,target_size=(216,216),detector_backend="opencv",enforce_detection=False)
    return faces

def find_face(face):
    recognition = DeepFace.find(img_path = face, db_path ="faces",enforce_detection=False,silent=True,threshold=0.4,detector_backend="opencv",model_name="OpenFace")
    id = recognition[0]["identity"].values
    dist = recognition[0]["distance"].values
    return id,dist

def get_info(face):
    info = DeepFace.analyze(img_path =face, actions = ['age', 'gender'],enforce_detection=False,silent=True,detector_backend="opencv")[0]
    age = info["age"]
    gender = info["dominant_gender"]
    return age,gender