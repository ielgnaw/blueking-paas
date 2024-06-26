<template>
  <div
    id="app"
    :style="{
      '--app-notice-height': `${isShowNotice ? GLOBAL.NOTICE_HEIGHT : 0}px`,
      '--app-content-pd': `${isShowNotice ? GLOBAL.NOTICE_HEIGHT + 50 : 50}px`
    }"
  >
    <!-- 通知中心 -->
    <notice-component
      v-if="isBkNotice"
      class="notice-cls"
      :api-url="apiUrl"
      @show-alert-change="showAlertChange"
    />
    <paas-header />
    <div
      style="min-height: calc(100% - 70px); overflow: auto;"
      :style="{'padding-top': `${pluginPaddingTop}px`}"
      :class="{ 'plugin-min-width': isPlugin }"
    >
      <router-view />
    </div>
    <paas-footer v-if="$route.meta.showPaasFooter" />
  </div>
</template>

<script>
import { bus } from '@/common/bus';
import paasHeader from '@/components/paas-header';
import paasFooter from '@/components/paas-footer';
import NoticeComponent from '@blueking/notice-component-vue2';
import '@blueking/notice-component-vue2/dist/style.css';

export default {
  components: {
    paasHeader,
    paasFooter,
    NoticeComponent,
  },
  data() {
    return {
      userInfo: {},
      showLoginModal: false,
      isPlugin: false,
      apiUrl: `${BACKEND_URL}/notice/announcements/`,
      loginWindow: null,
    };
  },
  computed: {
    isGray() {
      return ['myApplications', 'appLegacyMigration'].includes(this.$route.name);
    },
    isBkNotice() {
      return this.$store.state.userFeature?.BK_NOTICE;
    },
    isShowNotice() {
      return this.$store.state.isShowNotice;
    },
    pluginPaddingTop() {
      const routes = ['plugin', 'createPlugin'];
      if (this.isPlugin && this.isShowNotice && routes.includes(this.$route.name)) {
        return this.GLOBAL.NOTICE_HEIGHT;
      }
      return 0;
    },
  },
  watch: {
    $route: {
      handler(value) {
        this.isPlugin = value.path.includes('/plugin-center');
      },
      immediate: true,
    },
    isPlugin() {
      this.setGlobalBodyStyle();
    },
    showLoginModal(vlaue) {
      if (vlaue) {
        this.openLoginWindow();
      }
    },
  },
  created() {
    bus.$on('show-login-modal', () => {
      this.showLoginModal = true;
    });
    bus.$on('close-login-modal', () => {
      this.showLoginModal = false;
      setTimeout(() => {
        if (this.loginWindow) {
          this.loginWindow.close();
          this.loginWindow = null;
        }
        window.location.reload();
      }, 300);
    });
  },
  methods: {
    hideLoginModal() {
      this.showLoginModal = false;
    },
    // 公告列表change事件回调， isShow代表是否含有跑马灯类型公告
    async showAlertChange(isShow) {
      // 更新store数据
      const isShowNotice = isShow && this.isBkNotice;
      await this.$store.commit('updataNoticeStatus', isShowNotice);
    },
    // 插件开发者中心设置全局底色
    setGlobalBodyStyle() {
      document.body.style.backgroundColor = this.isPlugin ? '#F5F6FA' : '';
    },
    // 打开登录窗口
    openLoginWindow(w = 500, h = 420) {
      const loginCallbackURL = `${window.location.origin}/static/login_success.html?is_ajax=1`;
      const loginURL = `${window.GLOBAL_CONFIG.LOGIN_SERVICE_URL}/plain/?size=big&app_code=1&c_url=${loginCallbackURL}`;
      // 宽/高
      const screenWidth = window.screen.width;
      const screenHeight = window.screen.height;

      // 打开新窗口
      this.loginWindow = window.open(loginURL, '_blank', `
        width=${w},
        height=${h},
        top=${(screenHeight - h) / 2},
        left=${(screenWidth - w) / 2},
        channelmode=0,
        directories=0,
        fullscreen=0,
        location=0,
        menubar=0,
        resizable=0,
        scrollbars=0,
        status=0,
        titlebar=0,
        toolbar=0,
        close=0
    `);

      if (this.loginWindow) this.loginWindow.focus();
    },
  },
};
</script>

<style lang="scss">
    @import './assets/css/patch.scss';
    @import './assets/css/ps-style.scss';
    @import '~@/assets/css/mixins/dashed.scss';
    .notice-cls {
      position: fixed;
      top: 0px;
      left: 0px;
      height: 40px;
      width: 100%;
      z-index: 1001;
    }

    .gray-bg {
        background: #fafbfd;
    }

    .notice {
        position: fixed;
        left: 0px;
        top: 0px;
        width: 100%;
        z-index: 1001;
        text-align: center;
        line-height: 32px;
        background-color: #ff9600;
        color: #fff;
        max-height: 32px;
    }

    .plugin-min-width {
        min-width: 1366px;
    }

    .table-header-tips-cls {
        white-space: nowrap;
        text-overflow: ellipsis;
        overflow: hidden;
    }

    .success-dividing-line {
        position: relative;
        top: -1px;
        margin: 0 5px;
    }
</style>
