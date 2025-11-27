module.exports = {
  // 部署应用包时的基本URL
  publicPath: './',
  
  // 输出文件目录
  outputDir: 'dist',
  
  // 放置生成的静态资源的目录
  assetsDir: 'static',
  
  // 指定生成的index.html的输出路径
  indexPath: 'index.html',
  
  // 文件名哈希
  filenameHashing: true,
  
  // 是否在开发环境下通过 eslint-loader 在每次保存时 lint 代码
  lintOnSave: process.env.NODE_ENV === 'development',
  
  // 是否使用包含运行时编译器的 Vue 构建版本
  runtimeCompiler: false,
  
  // 生产环境是否生成 sourceMap 文件
  productionSourceMap: false,
  
  // webpack-dev-server 相关配置
  devServer: {
    port: 8080,
    open: true,
    overlay: {
      warnings: false,
      errors: true
    },
    // 配置代理
    proxy: {
      '/api': {
        target: 'http://localhost:3000',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  },
  
  // webpack 配置
  configureWebpack: {
    // 提供给应用的全局变量
    plugins: [
      // 可以在这里配置插件
    ],
    resolve: {
      alias: {
        '@': require('path').resolve(__dirname, 'src')
      }
    }
  },
  
  // 对 webpack 内部的配置进行更细粒度的修改
  chainWebpack: config => {
    // 可以在这里配置 webpack 链式操作
    // 例如：config.module.rule('vue').use('vue-loader').tap(options => { ... })
  },
  
  // css 相关配置
  css: {
    // 是否使用 css 分离插件 ExtractTextPlugin
    extract: process.env.NODE_ENV === 'production',
    // 是否启用 CSS source maps
    sourceMap: false,
    // 向 CSS 相关的 loader 传递选项
    loaderOptions: {
      css: {},
      postcss: {}
    },
    // 启用 CSS modules
    requireModuleExtension: true
  }
}