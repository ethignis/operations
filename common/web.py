def fetch_data():
    return ["/thermalgrabber_ros/image_color"]
    # return  ["/thermalgrabber_ros/image_mono8",
    #          "/thermalgrabber_ros/image_mono16",
    #          "/thermalgrabber_ros/image_deg_celsius"]

#data select from visual camera
def fetch_visual_data():
    # return ["/camera/image_color"]
    # return ["/camera/image_mono"]
    #return ["/thermalgrabber_ros/image_mono8","/camera/image_color"]
    return ["/thermalgrabber_ros/image_mono8"]