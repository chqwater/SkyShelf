<template>
  <div class="page-body">
    <div class="menu-bar">
      <ElMenu class="menu-vertical" default-active="1">
        <ElMenuItem index="1" @click="handleSearchAll">ALL</ElMenuItem>
        <ElMenuItem
          v-for="(item, index) in journey"
          :index="`${index + 2}`"
          @click="handleSearchCategory(index + 1)"
        >
          <span>{{ item }}</span>
        </ElMenuItem>
      </ElMenu>
    </div>
    <div class="box-container">
			<div class="tool-bar">
				<ElButton type="primary" style="margin-right: 20px;" :icon="Plus">Create Book</ElButton>
			</div>
      <div class="book-containner">
        <div class="book" v-for="book in 3" :key="book">
          <div class="cover">
            <div class="background">
              <img :src="book.img_url" />
            </div>
            <div class="actions">
              <button class="action-btn edit-btn">Edit</button>
              <button class="action-btn delete-btn">Delete</button>
            </div>
          </div>
          <div class="title">{{ book.title }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts" name="book-admin">
import { ElButton, ElMenu, ElMenuItem } from "element-plus";
import {
  Plus
} from '@element-plus/icons-vue';
import { journey } from "./journey";

const handleSearchAll = () => {
  console.log("all");
};
const handleSearchCategory = (id: any) => {
  console.log(id);
};
</script>

<style scoped>
.page-body {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: row;
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
}
.menu-bar {
  height: 100%;
  width: 200px;
  z-index: 999;
}
.menu-vertical {
  height: 100%;
}
.box-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
.tool-bar{
	width: 100%;
	height: 70px;
	display: flex;
	flex-direction: row;
	align-items: center;
	justify-content: end;
	position: fixed;
	top: 70px;
	right: 0%;
}
.book-containner {
  width: 100%;
  display: flex;
  flex-direction: row;
	margin-top: 60px;
}
.book {
  height: 250px;
  width: 150px;
  margin: 15px;
}
.cover {
  width: 100%;
  height: 220px;
  border-radius: 15px;
  margin: 0 0 10px 0;
  position: relative;
  overflow: hidden;
  cursor: pointer;
}
.background {
  width: 100%;
  height: 100%;
  transition: filter 0.3s ease;
}
.background img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.cover:hover .background {
  filter: blur(5px);
}
.actions {
  position: absolute;
  bottom: -50px;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-evenly;
  transition: transform 0.3s ease, opacity 0.3s ease;
  opacity: 0;
  z-index: 10;
}
.cover:hover .actions {
  transform: translateY(-50px);
  opacity: 1;
}
.action-btn {
  padding: 5px 10px;
  font-size: 14px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}
.edit-btn {
  background-color: #409eff;
  color: white;
}
.edit-btn:hover {
  background-color: #66b1ff;
}
.delete-btn {
  background-color: #f56c6c;
  color: white;
}
.delete-btn:hover {
  background-color: #ff8787;
}
</style>
