<template>
    <div class="sidebar">
        <ElMenu
            class="sidebar-el-menu"
            :default-active="onRoutes"
            :collapse="sidebar.collapse"
            router
        >
            <template v-for="item in menuData">
                <template v-if="item.children">
                    <ElSubMenu :index="item.index" :key="item.index">
                        <template #title>
                            <el-icon>
                                <component :is="item.icon"></component>
                            </el-icon>
                            <span>{{ item.title }}</span>
                        </template>
                        <template v-for="subItem in item.children">
                            <ElSubMenu
                                v-if="subItem.children"
                                :index="subItem.index"
                                :key="subItem.index"
                            >
                                <template #title>{{ subItem.title }}</template>
                                <ElMenuItem
                                    v-for="(threeItem, i) in subItem.children"
                                    :key="i"
                                    :index="threeItem.index"
                                >
                                    {{ threeItem.title }}
                                </ElMenuItem>
                            </ElSubMenu>
                            <el-menu-item v-else :index="subItem.index">
                                {{ subItem.title }}
                            </el-menu-item>
                        </template>
                    </ElSubMenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index" :key="item.index">
                        <ElIcon>
                            <component :is="item.icon"></component>
                        </ElIcon>
                        <template #title>{{ item.title }}</template>
                    </el-menu-item>
                </template>
            </template>
        </ElMenu>
        <div class="collapse-btn" @click="collapseChage">
          <el-icon v-if="sidebar.collapse">
            <Expand />
          </el-icon>
          <el-icon v-else>
            <Fold />
          </el-icon>
        </div>
    </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useSidebarStore } from '../store/sidebar';
import { useRoute } from 'vue-router';
import { onMounted } from 'vue';
import { menuData } from '../components/menu';
import { ElIcon, ElMenu, ElMenuItem, ElSubMenu } from 'element-plus';

const route = useRoute();
const onRoutes = computed(() => {
    return route.path;
});
const collapseChage = () => {
    sidebar.handleCollapse();
};
const sidebar = useSidebarStore();

onMounted(() => {
    if (document.body.clientWidth < 1500) {
        collapseChage();
    }
});
</script>

<style scoped >
.sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 70px;
    bottom: 50px;
    overflow-y: scroll;
    padding-top: 10px;
}
.collapse-btn {
	position: absolute;
	bottom: 0%;
	left: 10px;
  display: flex;
  justify-content: left;
  align-items: center;
  width: 100%;
  padding: 0 10px;
  cursor: pointer;
  opacity: 0.8;
  font-size: 22px;
}

.collapse-btn:hover {
    opacity: 1;
}
.sidebar::-webkit-scrollbar {
    width: 0;
}

.sidebar-el-menu:not(.el-menu--collapse) {
    width: 200px;
}

.sidebar-el-menu {
    min-height: 100%;
}
</style>
