<template>
  <div
    class="approve-container">
    <paas-content-loader
      :is-loading="loaderLoading"
      placeholder="order-loading"
      :offset-top="25"
      class="order-approve-wrapper"
    >
      <section v-show="!isLoading">
        <bk-tab
          class="mt5 audit-tab-cls"
          :active.sync="orderStatus"
          type="unborder-card"
        >
          <bk-tab-panel
            name="processing"
            :label="$t('未审批')"
          >
            <processing-order @data-ready="handlerDataReady" />
          </bk-tab-panel>
          <bk-tab-panel
            name="done"
            :label="$t('已审批')"
          >
            <done-order @data-ready="handlerDataReady" />
          </bk-tab-panel>
        </bk-tab>
      </section>
    </paas-content-loader>
  </div>
</template>

<script>import processingOrder from './processing-order';
import doneOrder from './done-order';
import appBaseMixin from '@/mixins/app-base-mixin';

export default {
  components: {
    processingOrder,
    doneOrder,
  },
  mixins: [appBaseMixin],
  data() {
    return {
      isLoading: false,
      loaderLoading: true,
      orderStatus: 'processing',
    };
  },
  computed: {
    curModule() {
      return this.curAppModuleList.find(item => item.is_default);
    },
  },
  watch: {
    '$route'() {
      this.$refs.moduleRef && this.$refs.moduleRef.setCurModule(this.curModule);
      // this.isLoading = true;
    },
  },
  mounted() {
    this.$refs.moduleRef && this.$refs.moduleRef.setCurModule(this.curModule);
  },
  methods: {
    setStatus(status) {
      this.orderStatus = status;
    },
    handlerDataReady() {
      this.isLoading = false;
      this.loaderLoading = false;
    },
  },
};

</script>

  <style lang="scss" scoped>
  .approve-container{
    min-height: calc(100% - 50px);
    .order-approve-wrapper{
      background: #fff;
      margin: 0;
    }
  }

      .ps-table-bar {
          padding: 20px 0;
      }

      .ps-checkbox-default {
          vertical-middle: top;
      }

      .ps-table td {
          padding: 14px 0 14px 20px;

          &:first-child {
              padding-left: 30px;
          }
      }
      .audit-tab-cls{
        margin: 10px 24px 0px;
      }
  </style>

