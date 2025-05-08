
# Sarassi SEO Bot

사라님의 티스토리 블로그를 위한 자동 SEO 도우미 봇입니다.

## 구성

- `blog_crawler.py`: 티스토리 블로그 글 목록 크롤링
- `slug_generator.py`: 제목 기반 슬러그 자동 생성
- `sitemap_generator.py`: sitemap.xml 자동 생성

## 사용 방법

1. 블로그 URL을 설정합니다.
2. `get_post_list()`로 글 링크를 수집합니다.
3. 필요 시 제목을 영어 슬러그로 변환합니다.
4. `generate_sitemap()`으로 sitemap.xml 생성 후 저장합니다.
5. 생성된 sitemap.xml을 GitHub Pages에 업로드 후 Search Console에 제출하세요.
