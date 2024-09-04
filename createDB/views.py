from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .DataProcessing.GetRouteData import (
    route_data_by_pk, 
    route_data_by_area, 
    route_data_by_tour_type, 
    route_data_by_tour_type_area
)
from .DataProcessing.TravelCharacter import recommend_character
from .DataProcessing.PersonalizedTypeCourse import recommend_course_view
from .DataProcessing.GroupSimilarityCourses import recommend_similar_group_view
from .DataProcessing.RandomRoute import random_area, random_tour_type

# 지역별 랜덤 관광지 추천 API
@swagger_auto_schema(
    method='get',
    operation_summary="지역별 랜덤 관광지 추천",
    operation_description="특정 지역 코드를 기반으로 랜덤한 관광지 5개를 추천합니다.",
    manual_parameters=[
        openapi.Parameter('areacode', openapi.IN_PATH, description="지역 코드 (예: 1 - 강릉)", type=openapi.TYPE_INTEGER),
    ],
    responses={
        200: openapi.Response(
            description="성공적으로 추천된 관광지 목록입니다.",
            examples={
                "application/json": {
                    "result": [
                        {
                            "model": "createDB.tours",
                            "pk": 461,
                            "fields": {
                                "sigungucode": 1,
                                "addr1": "강원특별자치도 강릉시 주문진읍 해안로 1960",
                                "addr2": "",
                                "image": "http://tong.visitkorea.or.kr/cms/resource/26/2709726_image2_1.jpg",
                                "cat1": "A05",
                                "cat2": "A0502",
                                "cat3": "A05020100",
                                "type_id": 39,
                                "mapx": 128.8297652402,
                                "mapy": 37.9047885414,
                                "title": "광순네",
                                "zipcode": "25407",
                                "tel": "010-9599-5460",
                                "eventstartdate": None,
                                "eventenddate": None
                            }
                        },
                        # 추가적인 관광지 데이터
                    ]
                }
            }
        ),
        400: "잘못된 요청입니다."
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_random_tours_by_area(request, areacode):
    try:
        random_tours = random_area(areacode)
        return Response({'result': random_tours}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 여행 선호 유형별 랜덤 관광지 추천 API
@swagger_auto_schema(
    method='get',
    operation_summary="여행 선호 유형별 랜덤 관광지 추천",
    operation_description="특정 지역과 여행 선호 유형을 기반으로 랜덤한 관광지 5개를 추천합니다.",
    manual_parameters=[
        openapi.Parameter('areacode', openapi.IN_PATH, description="지역 코드 (예: 1 - 강릉)", type=openapi.TYPE_INTEGER),
        openapi.Parameter('tour_type', openapi.IN_PATH, description="여행 선호 유형 (예: 힐링형 감자)", type=openapi.TYPE_STRING),
    ],
    responses={
        200: openapi.Response(
            description="성공적으로 추천된 관광지 목록입니다.",
            examples={
                "application/json": {
                    "result": [
                        {
                            "model": "createDB.tours",
                            "pk": 332,
                            "fields": {
                                "sigungucode": 1,
                                "addr1": "강원특별자치도 강릉시 죽헌동 745",
                                "addr2": "(죽헌동)",
                                "image": "http://tong.visitkorea.or.kr/cms/resource/09/2776909_image2_1.jpg",
                                "cat1": "A01",
                                "cat2": "A0101",
                                "cat3": "A01010500",
                                "type_id": 12,
                                "mapx": 128.8847557936,
                                "mapy": 37.7807456454,
                                "title": "경포생태저류지",
                                "zipcode": "25465",
                                "tel": "",
                                "eventstartdate": None,
                                "eventenddate": None
                            }
                        },
                        # 추가적인 관광지 데이터
                    ]
                }
            }
        ),
        400: "잘못된 요청입니다."
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_random_tours_by_tour_type(request, areacode, tour_type):
    try:
        random_tours = random_tour_type(areacode, tour_type)
        if isinstance(random_tours, str):  # 오류 메시지 처리
            return Response({"error": random_tours}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'result': random_tours}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 관광 계획 PK로 데이터 조회 API
@swagger_auto_schema(
    method='get',
    operation_summary="관광 계획 PK로 관광지 데이터 조회",
    operation_description="특정 관광 계획 PK를 기반으로 관광지 데이터를 조회합니다.",
    manual_parameters=[
        openapi.Parameter('route_pk', openapi.IN_PATH, description="관광 계획 PK", type=openapi.TYPE_INTEGER),
    ],
    responses={
        200: openapi.Response(
            description="성공적으로 조회된 관광지 목록입니다.",
            examples={
                "application/json": {
                    "result": [
                        # 추가적인 관광지 데이터
                    ]
                }
            }
        ),
        400: "잘못된 요청입니다."
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_route_data_by_route(request, route_pk):
    try:
        route_data = route_data_by_pk(route_pk)
        return Response({'result': route_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 특정 지역의 관광 계획 데이터 조회 API
@swagger_auto_schema(
    method='get',
    operation_summary="특정 지역의 관광 계획 데이터 조회",
    operation_description="특정 지역 코드에 해당하는 모든 관광 계획 데이터를 조회합니다.",
    manual_parameters=[
        openapi.Parameter('areacode', openapi.IN_PATH, description="지역 코드 (예: 1 - 강릉)", type=openapi.TYPE_INTEGER),
    ],
    responses={
        200: openapi.Response(
            description="성공적으로 조회된 관광 계획 목록입니다.",
            examples={
                "application/json": {
                    "result": [
                        # 추가적인 관광지 데이터
                    ]
                }
            }
        ),
        400: "잘못된 요청입니다."
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_routes_by_route_area(request, areacode):
    print(areacode)
    try:
        route_data = route_data_by_area(areacode)
        return Response({'result': route_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 특정 여행 유형의 관광 계획 데이터 조회 API
@swagger_auto_schema(
    method='get',
    operation_summary="특정 여행 유형의 관광 계획 데이터 조회",
    operation_description="특정 여행 유형에 맞는 관광 계획 데이터를 조회합니다.",
    manual_parameters=[
        openapi.Parameter('tour_type', openapi.IN_PATH, description="여행 유형 (예: 힐링형 감자)", type=openapi.TYPE_STRING),
    ],
    responses={
        200: openapi.Response(
            description="성공적으로 조회된 관광 계획 목록입니다.",
            examples={
                "application/json": {
                    "result": [
                        # 추가적인 관광지 데이터
                    ]
                }
            }
        ),
        400: "잘못된 요청입니다."
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_routes_by_tour_type(request, tour_type):
    try:
        route_data = route_data_by_tour_type(tour_type)
        return Response({'result': route_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 특정 지역과 여행 유형의 관광 계획 데이터 조회 API
@swagger_auto_schema(
    method='get',
    operation_summary="특정 지역과 여행 유형에 맞는 관광 계획 데이터 조회",
    operation_description="특정 지역과 여행 유형에 맞는 관광 계획 데이터를 조회합니다.",
    manual_parameters=[
        openapi.Parameter('areacode', openapi.IN_PATH, description="지역 코드 (예: 1 - 강릉)", type=openapi.TYPE_INTEGER),
        openapi.Parameter('tour_type', openapi.IN_PATH, description="여행 유형 (예: 힐링형 감자)", type=openapi.TYPE_STRING),
    ],
    responses={
        200: openapi.Response(
            description="성공적으로 조회된 관광 계획 목록입니다.",
            examples={
                "application/json": {
                    "result": [
                        # 추가적인 관광지 데이터
                    ]
                }
            }
        ),
        400: "잘못된 요청입니다."
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_routes_by_tour_type_area(request, areacode, tour_type):
    try:
        route_data = route_data_by_tour_type_area(areacode, tour_type)
        return Response({'result': route_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# 여행 유형별 관광 계획 데이터 조회 API
@swagger_auto_schema(
    method='get',
    operation_summary="여행 유형별 관광 계획 데이터 조회",
    operation_description="특정 여행 유형에 맞는 관광 계획 데이터를 조회합니다.",
    manual_parameters=[
        openapi.Parameter('tour_type', openapi.IN_QUERY, description="여행 유형 (예: 힐링형 감자)", type=openapi.TYPE_STRING),
    ],
    responses={
        200: openapi.Response(
            description="성공적으로 조회된 관광 계획 목록입니다.",
            examples={
                "application/json": {
                    "result": [
                        # 추가적인 관광지 데이터
                    ]
                }
            }
        ),
        400: "잘못된 요청입니다."
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_routes_by_tour_type(request, tour_type):
    try:
        route_data = route_data_by_tour_type(tour_type)
        return Response({'result': route_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 특정 지역과 여행 유형에 따른 관광 계획 데이터 조회 API
@swagger_auto_schema(
    method='get',
    operation_summary="특정 지역과 여행 유형에 맞는 관광 계획 데이터 조회",
    operation_description="특정 지역과 여행 유형에 맞는 관광 계획 데이터를 조회합니다.",
    manual_parameters=[
        openapi.Parameter('areacode', openapi.IN_QUERY, description="지역 코드 (예: 1 - 강릉)", type=openapi.TYPE_INTEGER),
        openapi.Parameter('tour_type', openapi.IN_QUERY, description="여행 유형 (예: 힐링형 감자)", type=openapi.TYPE_STRING),
    ],
    responses={
        200: openapi.Response(
            description="성공적으로 조회된 관광 계획 목록입니다.",
            examples={
                "application/json": {
                    "result": [
                        # 추가적인 관광지 데이터
                    ]
                }
            }
        ),
        400: "잘못된 요청입니다."
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_routes_by_tour_type_area(request, areacode, tour_type):
    try:
        route_data = route_data_by_tour_type_area(areacode, tour_type)
        return Response({'result': route_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 여행 유형 캐릭터 추천 API
@swagger_auto_schema(
    method='post',
    operation_summary="여행 유형 캐릭터 추천",
    operation_description="입력된 중요도 리스트를 기반으로 가장 적합한 여행 유형 캐릭터를 추천합니다.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'importance_list': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description="중요도 리스트 (예: [4, 2, 1, 4, 5, 6, 7, 8, 2, 0])"),
        },
        required=['importance_list']
    ),
    responses={
        200: openapi.Response(
            description="성공적으로 추천된 캐릭터 정보입니다.",
            examples={
                "application/json": {
                    "name": "도전형 인삼",
                    "description": "새로운 시도를 즐기며 끊임없이 도전하는 여행을 선호",
                    "recommended_place": "인제",
                    "reason": "도전을 즐기는 '인삼' 유형에게는 다양한 모험과 활동을 할 수 있는 인제가 적합합니다.",
                    "best_match": "액티비티형 옥수수",
                    "match_reason": "모험과 새로운 도전을 즐기는 두 유형은 함께 다양한 액티비티를 체험하며 에너지를 발산할 수 있는 여행을 즐길 수 있습니다."
                }
            }
        ),
        400: "잘못된 요청입니다."
    }
)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def recommend_character_view(request):
    try:
        importance_list = request.data.get('importance_list')
        if not isinstance(importance_list, list) or len(importance_list) != 10:
            return Response({"error": "중요도 리스트가 잘못되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

        character_info = recommend_character(importance_list)
        return Response({
            "name": character_info[0],
            "description": character_info[1],
            "recommended_place": character_info[2],
            "reason": character_info[3],
            "best_match": character_info[4],
            "match_reason": character_info[5]
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 개인 맞춤형 여행 코스 추천 API
@swagger_auto_schema(
    method='post',
    operation_summary="개인 맞춤형 여행 코스 추천",
    operation_description="입력된 중요도 리스트, 캐릭터 유형, 여행 지역을 기반으로 개인 맞춤형 여행 코스를 추천합니다.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'importance_list': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description="중요도 리스트 (예: [4, 3, 2, 5, 4, 2, 3, 1, 0, 5])"),
            'travel_character': openapi.Schema(type=openapi.TYPE_STRING, description="캐릭터 유형 (예: 힐링형 감자)"),
            'region': openapi.Schema(type=openapi.TYPE_STRING, description="여행 지역 (예: 강릉)"),
        },
        required=['importance_list', 'travel_character', 'region']
    ),
    responses={
        200: openapi.Response(
            description="성공적으로 추천된 여행 코스 목록입니다.",
            examples={
                "application/json": {
                    "result": [
                        {'title': '금강사(강릉)', 'addr1': '강원특별자치도 강릉시 연곡면 소금강길 670', 'mapx': 128.6909752621, 'mapy': 37.8062833683}, 
                        {'title': '기린사우나', 'addr1': '강원특별자치도 강릉시 남부로125번길 18', 'mapx': 128.8935561515, 'mapy': 37.7435306776}, 
                        # 추가적인 코스 데이터
                    ]
                }
            }
        ),
        400: "잘못된 요청입니다."
    }
)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def recommend_course_view(request):
    try:
        importance_list = request.data.get('importance_list')
        travel_character = request.data.get('travel_character')
        region = request.data.get('region')

        if not isinstance(importance_list, list) or len(importance_list) != 10:
            return Response({"error": "중요도 리스트가 잘못되었습니다."}, status=status.HTTP_400_BAD_REQUEST)
        if not travel_character or not region:
            return Response({"error": "캐릭터 유형 또는 여행 지역이 잘못되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

        recommended_courses = recommend_course_view(importance_list, travel_character, region)
        return Response({'result': recommended_courses}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 단체 유사도 기반 여행지 추천 API
@swagger_auto_schema(
    method='post',
    operation_summary="단체 유사도 기반 여행지 추천",
    operation_description="현재 그룹의 여행 선호도를 기반으로 유사한 그룹의 여행 코스를 추천합니다.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'current_group_id': openapi.Schema(type=openapi.TYPE_INTEGER, description="현재 그룹 ID"),
            'target_area': openapi.Schema(type=openapi.TYPE_STRING, description="여행 지역 (예: 강릉)"),
        },
        required=['current_group_id', 'target_area']
    ),
    responses={
        200: openapi.Response(
            description="성공적으로 추천된 유사 그룹의 여행 코스입니다.",
            examples={
                "application/json": {
                    "route_name": "route109",
                    "lodge": "lodge109",
                    "route_area": 1,
                    "tour_startdate": "2024-08-17T00:00:00Z",
                    "tour_enddate": "2024-08-18T00:00:00Z",
                    "group_id": 7,
                    "tour_info_list": [
                        {'title': '안인해변(안인해수욕장)', 'addr1': '강원특별자치도 강릉시 강동면 안인진리', 'mapx': 128.9904199396, 'mapy': 37.7343114116}, 
                        # 추가적인 코스 데이터
                    ]
                }
            }
        ),
        400: "잘못된 요청입니다."
    }
)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def recommend_similar_group_view(request):
    try:
        current_group_id = request.data.get('current_group_id')
        target_area = request.data.get('target_area')

        if not current_group_id or not target_area:
            return Response({"error": "그룹 ID 또는 여행 지역이 잘못되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

        similar_group_courses = recommend_similar_group_view(current_group_id, target_area)
        return Response(similar_group_courses, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_routes_data_by_route(request, route_pk):
    try:
        route_data = route_data_by_pk(route_pk)
        return Response({'result': route_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)