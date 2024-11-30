<template>
  <div class="page-box-book">
    <div class="app-header">
      <div class="home-btn">
        <ElBreadcrumb separator="/">
          <ElBreadcrumbItem :to="{path: '/home/booklist'}" style="font-size: 20px;"><p @click="handleSaveProgress">< My Shelf</p></ElBreadcrumbItem>
          <ElBreadcrumbItem v-if="isLoading"><p class="book-name">Loading...</p></ElBreadcrumbItem>
          <ElBreadcrumbItem v-else><p class="book-name">{{ route.query.name }}</p></ElBreadcrumbItem>
        </ElBreadcrumb>
      </div>
      <div class="tool-bar">
        <div class="page-number-jump" v-if="showJump">
          <ElInputNumber v-model="jumpPage" :min="1" :max="pageCount" style="margin-right: 5px;"/>
          <ElButton type="primary" @click="JumpToThePage">Jump</ElButton>
        </div>
        <div class="tool-btn" @click="handleJumpButton">
          <ElIcon :size="30"><Guide/></ElIcon>
        </div>
        <div class="tool-btn" @click="handleSaveProgress">
          <ElIcon :size="30"><Checked/></ElIcon>
        </div>
        <a class="tool-btn" :href="route.query.bookurl" download="book.pdf" target="_blank">
          <ElIcon :size="30"><Download/></ElIcon>
        </a>
      </div>
      <p class="page-info">{{ pageCount }} Pages in total</p>
    </div>
    <div class="app-content">
      <vue-pdf-embed
        ref="pdfRef"
        :source="route.query.bookurl"
        :page="page"
        @rendered="handleDocumentRender"
        height="800"
      />
      <vue-pdf-embed
        ref="secondpdfRef"
        :source="route.query.bookurl"
        :page="secondPage"
        @rendered="handleDocumentRender"
        height="800"
      />
      <ElIcon style="position: absolute; top: 50%; left:-10%; color: white; cursor: pointer;" size="80" @click="handlePreviousPage" class="btn" ><CaretLeft/></ElIcon>
      <ElIcon style="position: absolute; top: 50%; right:-10%; color: white; cursor: pointer;" size="80" @click="handleNextPage" class="btn" ><CaretRight/></ElIcon>
      <div style="position: absolute; top: -30px; left:0%; color: white; background-color: gray; border-radius: 10px; padding: 5px;">page {{ page }} </div>
      <div style="position: absolute; top: -30px; right:0%; color: white; background-color: gray; border-radius: 10px; padding: 5px">page {{ secondPage }}</div>
    </div>
    <el-progress :percentage="pagePercentage" :format="format" :text-inside="true" :stroke-width="6" type="circle" :width="90" style="position: fixed; top: 150px; right: 20px;" :show-text="true"/>
    <p style="position: fixed; top: 110px; right: 10px; color: white">Reading Percentage</p>
    <p style="position: fixed; top: 170px; right: 50px; color: white">{{ pagePercentage }}%</p>
  </div>
</template>

<script setup>
import { ElBreadcrumb, ElBreadcrumbItem, ElButton, ElDropdownMenu, ElIcon, ElInputNumber, ElMessage, ElProgress } from "element-plus";
import { ref, onMounted, watch, computed } from "vue";
import VuePdfEmbed from "vue-pdf-embed";
import { useRoute } from 'vue-router';
import { useRouter } from 'vue-router';
import { ElNotification as notify } from 'element-plus'
import { ElLoading } from 'element-plus';
import { saveProgress } from "../api";


const router = useRouter();
const route = useRoute();
const isLoading = ref(true);
const page = ref(null);
const secondPage = ref(null);
const pageCount = ref(1);
const showAllPages = ref(false);
const pdfRef = ref(null);
const secondpdfRef = ref(null);
const showJump = ref(false);
const jumpPage = ref(1);
const user_id = localStorage.getItem('vuems_id');

const handleJumpButton = ()=>{
  showJump.value = !showJump.value;
  jumpPage.value = page.value
}
const JumpToThePage = ()=>{
  if (jumpPage.value%2 === 0){
    page.value = jumpPage.value - 1;
  } else {
    page.value = jumpPage.value;
  }
  secondPage.value = page.value + 1;
}
const loading = ElLoading.service({
    lock: true,
    text: 'Loading',
    background: 'rgba(255, 255, 255, 0.7)',
  })

const format = (percentage) => (percentage === 100 ? 'Finish' : `${percentage}%`)
const pagePercentage = computed(()=>{
  const percentage = (page.value / pageCount.value) * 100;
  return Math.round(percentage);
})

const handleNextPage = () => {
  if ( page.value + 1 >= pageCount.value){
    ElMessage.warning('This is the last page!');
    return;
  }
  page.value = page.value + 2;
  secondPage.value = secondPage.value + 2;
};
const handlePreviousPage = () => {
  if (page.value <= 1) {
    ElMessage.warning('This is the first page!');
    return;
  }
  page.value = page.value - 2;
  secondPage.value = secondPage.value - 2;
};
const saveReadProgress = async ()=>{
  const loading2 = ElLoading.service({
    lock: true,
    text: 'Loading',
    background: 'rgba(0, 0, 0, 0.7)',
  })
  await saveProgress({
    user_id: Number(user_id),
    book_id: Number(route.query.bookid),
    last_read_position: Number(page.value)
  }).then(res =>{
    console.log('saved at page' + page.value);
    loading2.close();
    notify({
    title: 'Reading Progress Saved for ' + route.query.name,
    duration: 3000,
    message: 'Dont worry! You will continue from the page you left.',
    type: 'success',
    offset: 60
    });
  })
}
function handleDocumentRender(args) {
  console.log("pdf loaded");
  isLoading.value = false;
  pageCount.value = pdfRef.value.pageCount;
  loading.close();
}

const handleSaveProgress = ()=>{
  saveReadProgress();
}
watch(showAllPages, () => {
  page.value = showAllPages.value ? null : 1;
});

onMounted(() => {
  page.value = parseInt(route.query.currentPage, 10)%2 == 0 ? parseInt(route.query.currentPage, 10) - 1 : parseInt(route.query.currentPage, 10);
  secondPage.value = page.value + 1;
  console.log("data loaded");
  console.log(route.query);
});
</script>

<style scoped>
.page-box-book {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url(../assets/img/book-bg.jpg) center/cover no-repeat;
}
.page-box-book::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.4);
  z-index: 1;
}

.page-box-book > * {
  position: relative;
  z-index: 2;
}
.app-content {
  width: 1135px;
  display: flex;
  flex-direction: row;
  border: 5px solid gray;
  margin-left: calc((100% - 1130px) / 2);
  background-color: white;
  justify-content: center;
  margin-top: 30px;
  position: relative;
  min-height: 800px;
}
.app-header {
  width: 100%;
  height: 90px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: rgb(255, 255, 235);
  box-shadow: 0 4px 6px rgba(87, 87, 87, 0.2); 
  position: relative;
}
.btn{
  border: 2px solid white;
  border-radius: 50%;
}
.btn:hover{
  box-shadow: 0 0 90px rgba(64, 158, 255, 1.5), inset 0 0 15px rgba(94, 69, 159, 0.4); 
}
.home-btn{
  position: absolute;
  top: 30%;
  left: 20px;
  cursor: pointer;
  font-size: 20px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-weight: 600;
  color: rgb(90, 90, 90);
}
.home-btn:hover{
  color: #409EFF;
}
.book-name{
  font-family: cursive;
  font-size: 28px;
  color: rgb(90, 90, 90);
  font-weight: 1000;
  height: 60px;
  margin-bottom: 0%;
  margin-top: 10px;
}
.page-info{
  font-size: 16px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  color: rgb(76, 76, 76);
}
.tool-bar{
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: end;
  align-items: center;
  min-height: 52px;
}
.tool-btn{
  color: rgb(90, 90, 90);
  border-radius: 50px;
  border: 1px solid rgb(90, 90, 90);
  margin-right: 10px;
  width: 30px;
  height: 30px;
  cursor: pointer;
}
.tool-btn:hover{
  color: #409EFF;
  border: 1px solid #409EFF;
}
.page-number-jump{
  background-color: white;
  padding: 10px;
  border-radius: 15px;
}
</style>
