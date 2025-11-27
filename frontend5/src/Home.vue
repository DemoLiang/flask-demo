<template>
  <div>
    <h1>简单数据图表</h1>
    <div id="chart" style="width: 100%; height: 400px;"></div>
    <button @click="refreshData" style="margin-top: 20px;">刷新数据</button>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import { getChartData } from './api';

export default {
  name: 'Home',
  data() {
    return {
      chart: null
    };
  },
  mounted() {
    // 初始化图表
    this.chart = echarts.init(document.getElementById('chart'));
    // 初始化时获取数据
    this.refreshData();
    // 窗口大小改变时重新调整图表大小
    window.addEventListener('resize', () => this.chart.resize());
  },
  beforeUnmount() {
    // 清理事件监听
    window.removeEventListener('resize', () => this.chart.resize());
  },
  methods: {
    // 刷新数据
    async refreshData() {
      try {
        // 从API获取数据
        const newData = await getChartData();
        
        // 设置图表选项
        const option = {
          title: { text: '数据趋势' },
          xAxis: { type: 'category', data: newData.categories },
          yAxis: { type: 'value' },
          series: [{
            type: 'line',
            data: newData.values
          }]
        };
        
        // 更新图表
        this.chart.setOption(option);
      } catch (error) {
        console.log('数据更新失败:', error);
      }
    }
  }
};
</script>