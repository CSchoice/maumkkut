# character_recommendations.py

characters = [
    {
        "name": "힐링형 감자",
        "keywords": {"힐링": 5, "여유로움": 5, "자연": 5, "관람": 2, "음식점": 1, "모험": 1, "액티비티":1,"사람 많은 곳": 1, "쇼핑": 1, "사진 촬영": 2},
        "description": "조용하고 평화로운 환경을 선호, 주로 힐링을 목적으로 한 여행을 즐김",
        "recommended_place": "정선",
        "reason": "자연 속에서 여유롭게 시간을 보내는 것을 선호하는 '힐링형 감자'에게는 산과 강이 어우러진 정선이 잘 어울립니다.",
        "best_match": "나무늘보형 순두부",
        "match_reason": "두 유형 모두 조용하고 여유로운 여행을 선호하며, 자연 속에서 힐링할 수 있는 시간을 즐깁니다. 서로의 페이스에 맞추어 편안한 여행을 할 수 있습니다."

    },
    {
        "name": "액티비티형 옥수수",
        "keywords": {"힐링": 1, "여유로움": 2, "자연": 4, "관람": 2, "음식점": 3, "모험": 5, "액티비티":5, "사람 많은 곳": 5, "쇼핑": 2, "사진 촬영": 4},
        "description": "모험과 활동적인 여행을 즐김, 다양한 액티비티 체험을 선호",
        "recommended_place": "양양",
        "reason": "액티비티를 즐기고 모험을 사랑하는 '옥수수' 유형에게 양양은 서핑과 같은 액티비티를 즐길 수 있는 최적의 장소입니다.",
        "best_match":"도전형 인삼",
        "match_reason": "모험과 활동을 좋아하는 두 유형은 다양한 액티비티를 함께 즐기며 시너지 효과를 낼 수 있습니다. 둘 다 도전적인 여행을 즐기기에 잘 어울립니다."
    },
    {
        "name": "관람형 곤드레",
        "keywords": {"힐링": 2, "여유로움": 3, "자연": 3, "관람": 5, "음식점": 3, "모험": 2, "액티비티":2, "사람 많은 곳": 2, "쇼핑": 3, "사진 촬영": 4},
        "description": "문화와 역사에 관심이 많아 박물관, 미술관 등을 자주 방문",
        "recommended_place": "평창",
        "reason": "문화와 역사를 중시하는 '곤드레' 유형에게는 올림픽 관련 관광지와 자연의 조화가 돋보이는 평창이 어울립니다.",
        "best_match":"미식가형 송이",
        "match_reason":"두 유형은 문화와 음식에 관심이 많으며, 박물관이나 문화유산 탐방 후 지역 맛집에서 식사를 즐길 수 있습니다. 서로의 관심사를 공유하며 알찬 여행을 할 수 있습니다."
    },
    {
        "name": "미식가형 송이",
        "keywords": {"힐링": 2, "여유로움": 4, "자연": 2, "관람": 3, "음식점": 5, "모험": 2, "액티비티":3,"사람 많은 곳": 4, "쇼핑": 4, "사진 촬영": 3},
        "description": "맛집 탐방과 음식을 즐기는 여행을 선호",
        "recommended_place": "춘천",
        "reason": "맛집 탐방과 음식을 즐기는 '황태' 유형에게 춘천은 다양한 맛집이 있어 미식 여행을 즐기기에 적합한 곳입니다.",
        "best_match":"관람형 곤드레",
        "match_reason":"맛집 탐방과 문화 관람을 함께 즐길 수 있는 두 유형은 여행 중 자연스럽게 서로의 취향을 반영한 일정을 만들 수 있어 서로에게 긍정적인 영향을 줍니다."
    },
    {
        "name": "사람좋아 쌀알",
        "keywords": {"힐링": 1, "여유로움": 2, "자연": 4, "관람": 2, "음식점": 3, "모험": 3, "액티비티":4,"사람 많은 곳": 5, "쇼핑": 4, "사진 촬영": 4},
        "description": "사람들이 많이 모이는 곳을 선호하고 활기찬 분위기를 즐김",
        "recommended_place":"속초",
        "reason":"활기찬 분위기를 좋아하고 많은 사람들과 함께하는 것을 즐기는 '쌀알' 유형에게는 북적이는 해변과 시장이 있는 속초가 잘 어울립니다.",
        "best_match":"인플루언서형 복숭아",
        "match_reason":""
    },
    {
        "name": "도전형 인삼",
        "keywords": {"힐링": 2, "여유로움": 3, "자연": 5, "관람": 3, "음식점": 3, "모험": 5, "액티비티":5, "사람 많은 곳": 2, "쇼핑": 2, "사진 촬영": 4},
        "description": "새로운 시도를 즐기며 끊임없이 도전하는 여행을 선호",
        "recommended_place":"인제",
        "reason":"도전을 즐기는 '인삼' 유형에게는 다양한 모험과 활동을 할 수 있는 인제가 적합합니다.",
        "best_match":"액티비티형 옥수수",
        "match_reason":"모험과 새로운 도전을 즐기는 두 유형은 함께 다양한 액티비티를 체험하며 에너지를 발산할 수 있는 여행을 즐길 수 있습니다."
    },
    {
        "name": "인플루언서형 복숭아",
        "keywords": {"힐링": 1, "여유로움": 2, "자연": 3, "관람": 3, "음식점": 4, "모험": 3, "액티비티":3, "사람 많은 곳": 5, "쇼핑": 5, "사진 촬영": 4},
        "description": "핫한 장소를 찾아다니며, 새로운 트렌드를 즐기고 공유",
        "recommended_place":"양양",
        "reason":"트렌디한 장소를 즐기는 '복숭아' 유형에게는 최근 핫한 장소로 떠오르고 있는 양양이 잘 맞습니다.",
        "best_match":"사람좋아 쌀알",
        "match_reason":"트렌디한 장소를 찾아다니며 새로운 경험을 공유하는 것을 좋아하는 '복숭아' 유형과, 사람들과 함께하는 활기찬 분위기를 즐기는 '쌀알' 유형은 서로의 여행 스타일을 즐기며 시너지를 낼 수 있습니다."
    },
    {
        "name": "나무늘보형 순두부",
        "keywords": {"힐링": 4, "여유로움": 5, "자연": 3, "관람": 2, "음식점": 3, "모험": 1, "액티비티":1, "사람 많은 곳": 1, "쇼핑": 1, "사진 촬영": 2},
        "description": "일정에 구애받지 않고 여유로운 여행을 선호",
        "recommended_place":"영월",
        "reason":"일정에 구애받지 않고 여유롭게 여행을 즐기고 싶은 '순두부' 유형에게는 한적한 영월이 적합합니다.",
        "best_match":"힐링형 감자",
        "match_reason":"일정에 구애받지 않고 여유로운 여행을 선호하는 두 유형은 자연 속에서 조용히 힐링하며 느긋한 여행을 함께 즐길 수 있습니다."
    }
]