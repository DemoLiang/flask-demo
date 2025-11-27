// 使用fetch请求接口的API模块
export async function getChartData() {
  try {
    // 使用JSONPlaceholder的公开API作为测试接口
    const response = await fetch('https://jsonplaceholder.typicode.com/posts');
    
    // 检查响应状态
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    // 获取数据
    const posts = await response.json();
    
    // 将返回的数据转换为图表需要的格式
    // 取前9条数据，使用id作为值，title作为分类
    const categories = posts.slice(0, 9).map(post => post.title.substring(0, 10) + '...');
    const values = posts.slice(0, 9).map(post => post.id * 10);
    
    return {
      categories,
      values
    };
  } catch (error) {
    console.error('获取数据失败:', error);
    // 如果请求失败，返回默认数据
    return {
      categories: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月'],
      values: [120, 200, 150, 80, 70, 110, 130, 170, 140]
    };
  }
}
