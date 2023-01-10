# 함수를 사용한 프로그램 설계
'''
1. 요구사항이 들어오면 철저히 분석한다.(요구사항 명세서, 사규, 데이터 등)
2. 문제를 한번에 해결하려하지말고 작은 크기의 문제를 분류판별한다. 충분히 작아질때까지 지속적 분해
3. 분해가 되지않는 그러한 부분에 도달을했을때 비로소 기능을 함수로 만들어 조립, 최종적인 프로그램 완성
4. 솔루션(solution)을 단위테스트 및 통합테스트까지 완료, 회사에 배포를 하고 안정화를 시켜줘야함
'''
# grade.py 모듈을 ex14.py 파일에서 사용하겠다 라고 인터프리터에게 알림
import grade

def main():
    score_list = grade.readList()
    score_list = grade.sorting_list(score_list)
    grade.show_score(score_list)


if __name__ == "__main__":
    main()