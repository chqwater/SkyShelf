<template>
  <div class="page-box-book" v-loading.fullscreen.lock="isLoading">
    <div class="app-header" v-if="isLoading">
      <div class="home-btn" @click="handleBackToShelf"><ElIcon size="15"><CaretLeft/></ElIcon>Back to my shelf</div>
      <p class="book-name">Loading...</p>
    </div>
    <div class="app-header" v-else>
      <div class="home-btn" @click="handleBackToShelf"><ElIcon size="15"><CaretLeft/></ElIcon>Back to my shelf</div>
      <p class="book-name">{{ route.query.name }}</p>
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
      <ElIcon style="position: absolute; top: 50%; left:-8%; color: white; cursor: pointer;" size="80" @click="handlePreviousPage" class="btn" ><CaretLeft/></ElIcon>
      <ElIcon style="position: absolute; top: 50%; right:-8%; color: white; cursor: pointer;" size="80" @click="handleNextPage" class="btn" ><CaretRight/></ElIcon>
      <div style="position: absolute; top: -30px; left:0%; color: white; background-color: gray; border-radius: 10px; padding: 5px;">page {{ page }} </div>
      <div style="position: absolute; top: -30px; right:0%; color: white; background-color: gray; border-radius: 10px; padding: 5px">page {{ secondPage }}</div>
    </div>
  </div>
</template>

<script setup>
import { ElButton, ElIcon, ElMessage } from "element-plus";
import { ref, onMounted, watch } from "vue";
import VuePdfEmbed from "vue-pdf-embed";
import { useRoute } from 'vue-router';
import { useRouter } from 'vue-router';
import { ElNotification as notify } from 'element-plus'

const router = useRouter();
const route = useRoute();
const isLoading = ref(true);
const page = ref(null);
const secondPage = ref(null);
const pageCount = ref(1);
const showAllPages = ref(false);
const pdfRef = ref(null);
const secondpdfRef = ref(null);


const handleBackToShelf = ()=>{
  router.push('/home/booklist');
  notify({
    title: 'Reading Progress Saved for ' + route.query.name,
    duration: 3000,
    message: 'Dont worry! You will continue from the page you left.',
    type: 'success',
    offset: 60
  })
}
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

function handleDocumentRender(args) {
  console.log("pdf loaded");
  isLoading.value = false;
  pageCount.value = pdfRef.value.pageCount;
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
  top: 40%;
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
.el-loading-mask {
  z-index: 9999;
}
</style>
