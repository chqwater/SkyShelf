<template>
    <div class="content-box-reco">
      <div class="search-bar">
        <el-input style="width: 800px"
      size="large"
      placeholder="Search book here"
      :suffix-icon="Search"></el-input>
      </div>
    </div>
</template>

<script setup lang="ts" name="recommendation">
import { Search } from '@element-plus/icons-vue'
</script>

<style>
.content-box-reco{
    width: 100%;
    height: 100%;
    display: flex;
}
.search-bar{
    width: 100%;
    height: 70px;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>