def get_region_code(region_name):
    region_codes = {
        "강릉": 1, "고성": 2, "동해": 3, "삼척": 4, "속초": 5, "양구": 6, "양양": 7, 
        "영월": 8, "원주": 9, "인제": 10, "정선": 11, "철원": 12, "춘천": 13, 
        "태백": 14, "평창": 15, "홍천": 16, "화천": 17, "횡성": 18
    }
    
    return region_codes.get(region_name, "해당 지역의 코드가 없습니다.")
