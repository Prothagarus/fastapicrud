<script lang="ts">
import { defineComponent } from 'vue';
import { TabulatorFull as Tabulator } from 'tabulator-tables'; //import Tabulator library
import { DateTime } from 'luxon'
import { type RowComponent, type CellComponent } from 'tabulator-tables'

interface ToDoGet {
    id: string
    task: string
}
interface Taskdropdown {
    task: string
}

export default defineComponent({
    data() {
        return {
            tabulator: null, //variable to hold your table
            tableData: [] as Array<ToDoGet>, //data for table to display
            taskdropdown: [] as Array<Taskdropdown>,
            savedata: [] as Array<ToDoGet>
        }
    },
    methods: {
        gettabledata() {
            this.tableData = []
            fetch('http://localhost:8043/ToDoGet').then((d) => d.json().then((d2: Array<ToDoGet>) => { this.tableData = d2 }))

        },
        getdropdownlist() {
            fetch('http://localhost:8043/ToDoGet_DropdownList')
                .then((response) => response.json())
                .then((data) => {
                    this.taskdropdown = data;
                })
        },
        persisttablechangestobuffer() {
            this.savedata = [] as Array<ToDoGet>
            let rowdata = new Set<RowComponent>()
            let buf: Array<CellComponent> = this.tabulator.getEditedCells()
            buf.forEach((c: CellComponent) => {
                rowdata.add(c.getRow())
            })
            rowdata.forEach((e: RowComponent) => { this.savedata.push(e.getData()) })
        },
        savetodatabase() {

        }






    },

    mounted() {
        this.taskdropdown = this.getdropdownlist()
        //instantiate Tabulator when element is mounted
        this.tabulator = new Tabulator(this.$refs.table, {
            data: this.gettabledata(), //link data to table
            reactiveData: true, //enable data reactivity
            columns: [{ title: 'id', field: 'id' },
            {
                title: 'task',
                field: 'task',
                editor: "select",
                editorParams: () => {
                    let dropdownOptions = {};
                    this.taskdropdown.forEach((option) => {
                        dropdownOptions[option.task] = option.task;
                    });
                    return { values: dropdownOptions };
                }
                //define table columns
            ]
        });
    }
})
</script>

<template>
    <div ref="table"></div>
</template>